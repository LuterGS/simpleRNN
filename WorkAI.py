import requests
from NeuralNetwork import RNN as nn
from DB import sqlite_set
import datetime
import pandas_datareader.data as web

class Worker:

    data_type = ["KOSPI", "USD", "CHN"]

    def __init__(self):
        self.__rnn = [nn.RNN(25, name) for name in self.data_type]
        for i in range(3):
            self.result = [self.__rnn[i].predict_db(sqlite_set.get_db_data(type=self.data_type[i], wishdate=datetime.datetime.now()))[0][0] for i in range(3)]
        self.cur_time = datetime.datetime.now()

    def __get_today_prediction(self, cur_time):
        for i in range(3):
            self.result = [self.__rnn[i].predict_db(sqlite_set.get_db_data(type=self.data_type[i], wishdate=cur_time))[0][0] for i in range(3)]

    def __get_today_value(self, cur_time):
        # 오늘의 값을 받아와 DB에 저장하는 부분
        cur_time_str = cur_time.strftime('%Y%m%d')
        request_string = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=1pVEJgR09PqdC2LZ9syG0TVSZ77rVYaL&searchdate=" + cur_time_str + "&data=AP01"
        result = requests.get(request_string).json()
        kospi_request = round(web.get_data_yahoo("^KOSPI").values.tolist()[0][-1], 2)
        try:
            for i in range(len(result)):
                if result[i]['cur_nm'] == "미국 달러":
                    usd = float(result[i]['deal_bas_r'].replace(",", ""))
                if result[i]['cur_nm'] == "위안화":
                    chn = float(result[i]['deal_bas_r'].replace(",", ""))
            sqlite_set.save_today_data(cur_time, usd, "usd")
            sqlite_set.save_today_data(cur_time, chn, "chn")
            sqlite_set.save_today_data(cur_time, kospi_request, "kospi")
        except:
            pass



    def __save_prediction(self, cur_time):
        sqlite_set.save_prediction_data(self.result, cur_time)


    def work_oneday(self):
        cur_time = datetime.datetime.now()
        print("Working on get data")
        self.__get_today_value(cur_time)
        self.__get_today_prediction(cur_time)
        self.__save_prediction(cur_time)


if __name__ == "__main__":
    test = Worker()
    test.work_oneday()
