import requests
import datetime
import csv
from customLibrary import library


def get_exchange_rate():
    date = datetime.datetime(2000, 1, 1)
    write_data = open('환율_v3.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(write_data)
    csv_writer.writerow(["연도", "미국 환율", "미국 증감값", "미국 증감률", "중국 환율", "중국 증감값", "중국 증감률"])

    date_string = date.strftime('%Y%m%d')
    request_string = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=1pVEJgR09PqdC2LZ9syG0TVSZ77rVYaL&searchdate=" + date_string + "&data=AP01"
    result = requests.get(request_string)
    result = result.json()
    china, america = float(result[7]['deal_bas_r'].replace(",", "")), float(result[-2]['deal_bas_r'].replace(",", ""))
    csv_writer.writerow([date_string, america, china])
    date = date + datetime.timedelta(days=1)

    while True:
        prev_america, prev_china = america, china
        date_string = date.strftime('%Y%m%d')
        print(date_string)
        request_string = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=1pVEJgR09PqdC2LZ9syG0TVSZ77rVYaL&searchdate=" + date_string + "&data=AP01"
        result = requests.get(request_string)
        result = result.json()
        if result == [] or result[0]['result'] != 1:
            pass
        else:
            for i in range(len(result)):
                if result[i]["cur_unit"] == "CNY":
                    china_num = i
                if result[i]["cur_unit"] == "USD":
                    america_num = i

            china, america = float(result[china_num]['deal_bas_r'].replace(",", "")), float(
                result[america_num]['deal_bas_r'].replace(",", ""))
            america_value, america_percent = library.ud_value_percent(prev_america, america)
            china_value, china_percent = library.ud_value_percent(prev_china, china)
            csv_writer.writerow(
                [date_string, america, america_value, america_percent, china, china_value, china_percent])

        if date_string == "20200515":
            break

        date = date + datetime.timedelta(days=1)

    write_data.close()

if __name__ == "__main__":

    print("Hello World")
    get_exchange_rate()
