import datetime
import os
import sqlite3
from customLibrary import library

filepath = os.path.dirname(os.path.realpath(__file__))[:-2]


def get_db_data(type="kospi", wishdate=datetime.datetime.now(), past=25):
    # print(filepath)
    connection = sqlite3.connect(filepath + "Data/data.db")
    cursor = connection.cursor()
    date_string = library.get_pastdays_as_list(wishdate, pastdays=past * 2)
    # print(date_string)
    result = []
    # print(type)

    strs = "select * from " + str(type) + " where date=" + "\'" + date_string[0] + "\'"
    # print(strs)

    for i in range(past * 2):
        cursor.execute("select * from " + type + " where date=" + "'" + date_string[i] + "'")
        date_data = cursor.fetchall()
        if date_data != []:
            result.append(date_data[0][1])
        if len(result) == past:
            break
    connection.close()
    result.reverse()
    # print(result)
    return result


def save_today_data(cur_time, value, type="kospi"):
    connection = sqlite3.connect(filepath + "Data/data.db")
    cursor = connection.cursor()
    cur_time = cur_time.strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO " + type + " (date, value) values('" + cur_time + "', '" + str(value) + "');")
    connection.commit()
    connection.close()


def save_prediction_data(predict_result, cur_time):
    connection = sqlite3.connect(filepath + "Data/data.db")
    cursor = connection.cursor()
    cur_time_string = cur_time.strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO prediction (date, kospi, usd, chn) values('" + cur_time_string + "', '" + str(predict_result[0]) + "', '" + str(predict_result[1]) + "', '" + str(predict_result[2]) + "');")
    connection.commit()
    connection.close()


if __name__ == "__main__":
    get_db_data()
