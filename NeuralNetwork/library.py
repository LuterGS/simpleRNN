import csv
import random
import numpy as np


def set_datapath(type="KOSPI"):
    if type == "KOSPI":
        file_path, col_num = '../Data/csv/코스피지수.csv', 1
    elif type == "USD":
        file_path, col_num = '../Data/csv/환율_v2_fortest.csv', 1
    elif type == "CHN":
        file_path, col_num = '../Data/csv/환율_v2_fortest.csv', 4
    return file_path, col_num


def get_data(prev, type="KOSPI"):
    """
        :param prev: 며칠 전까지의 데이터를 참고할 것인지에 대한 값
        :return:
        """
    file_path, col_num = set_datapath(type)
    kospi_file = open(file_path, "r")
    csv_reader = csv.reader(kospi_file)
    csv_reader.__next__()
    csv_reader.__next__()
    data = []
    temp_data, input_data, answer_data = [], [], []

    for line in csv_reader:
        data.append(float(line[col_num]))
    data = normalization_data(data)

    if type == "KOSPI":
        data.reverse()

    total_length = len(data) - prev

    for i in range(total_length - 10):
        temp_x = []
        for j in range(prev + 1):
            temp_x.append(data[i + j])
        temp_data.append(temp_x)
    random.shuffle(temp_data)

    for i in range(total_length - 10):
        answer_data.append(temp_data[i].pop())
        input_data.append(np.transpose(np.asarray(temp_data[i]).reshape(1, prev)).tolist())

    input_data = np.asarray(input_data)
    answer_data = np.asarray(answer_data)

    return input_data, answer_data


def normalization_data(data):
    data = np.asarray(data)
    # print(data.min(), data.max() - data.min())
    data = (data - data.min()) / (data.max() - data.min())
    return data.tolist()


def de_normalization_data(data, data_type):
    if data_type == "KOSPI":
        return data * 2129.43 + 468.76
    elif data_type == "USD":
        return data * 690.3 + 902.7
    elif data_type == "CHN":
        return data * 113.71 + 116.21


def normalization_db_data(data, data_type="KOSPI"):

    if data_type == "KOSPI":
        max_min, min = 2129.43, 468.76
    elif data_type == "USD":
        max_min, min = 690.3, 982.7
    else:
        max_min, min = 113.71, 116.21

    for i in range(len(data)):
        data[i] = (data[i] - min) / max_min
    data = np.asarray([np.transpose(np.asarray(data).reshape(1, len(data))).tolist()])
    print(data.shape)
    # print(data)
    return data


if __name__ == "__main__":
    get_data(10, "CHN")
