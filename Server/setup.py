from NeuralNetwork import RNN as nn
from DB import sqliteSet
import datetime

class Worker:

    data_type = ["KOSPI", "USD", "CHN"]

    def __init__(self):
        self.__rnn = [nn.RNN(25, name) for name in self.data_type]

    def __get_today_prediction(self):
        self.cur_time = datetime.datetime.now()
        for i in range(3):
            self.__result = [self.__rnn[i].predict_db(sqliteSet.get_db_data(type=self.data_type[i], wishdate=cur_time)) for i in range(3)]

    def __get_today_value(self):
        # 오늘의 값을 받아오는 부분
        get_today = 0

    def __save_prediction(self):
        sqliteSet.save_prediction_data(self.__result, self.cur_time)


    def work_oneday(self):
        self.__get_today_value()
        self.__get_today_prediction()
        self.__save_prediction()
        # return self.__result




if __name__ == "__main__":

    test = nn.RNN(25)
    get_data = sqliteSet.get_db_data(type="kospi", wishdate=datetime.datetime(2020, 5, 15))
    test.predict_db(get_data)

