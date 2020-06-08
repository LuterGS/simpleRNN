import csv, sqlite3
from customLibrary import library as customLibrary


def kospi_into_db():

    file = open("../Data/csv/코스피지수.csv", "r")
    csv_reader = csv.reader(file)
    connection = sqlite3.connect("../Data/data.db")
    cursor = connection.cursor()

    for line in csv_reader:

        # print(line)
        if line[0] == "날짜":
            print("연도임")
        else:
            data = customLibrary.kospi_csv_date_to_string(line[0])
            cursor.execute("INSERT INTO kospi (date, value) VALUES('" + str(data) + "', " + line[1] + ");")
            connection.commit()

    cursor.execute("select * from kospi")


def usd_chn_into_db():
    file = open("../Data/csv/환율_v2.csv", "r")
    csv_reader = csv.reader(file)
    connection = sqlite3.connect("../Data/data.db")
    cursor = connection.cursor()

    for line in csv_reader:

        # print(line)
        if line[0] == "연도":
            print("연도임")
        else:
            data = customLibrary.usd_chn_date_to_string(line[0])
            print(data)
            cursor.execute("INSERT INTO usd (date, value) VALUES('" + str(data) + "', " + line[1] + ");")
            connection.commit()
            cursor.execute("INSERT INTO chn (date, value) VALUES('" + str(data) + "', " + line[4] + ");")
            connection.commit()


if __name__ == "__main__":

    usd_chn_into_db()




