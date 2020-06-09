import datetime


def kospi_csv_date_to_string(data):
    return "-".join([strings[:-1] for strings in data.split(" ")])

def usd_chn_date_to_string(data):
    return data[0:4] + "-" + data[4:6] + "-" + data[6:8]


def ud_value_percent(prev, cur):

    #print(prev, cur)
    value = round(cur - prev, 2)
    percent = round(((cur / prev) - 1) * 100, 2)

    return value, percent


def ud_percent(prev, cur):

    _, output = ud_value_percent(prev, cur)
    return output


def get_pastdays_as_list(date, pastdays=25, value=[]):

    for i in range(pastdays):
        value.append((date - datetime.timedelta(days=i)).strftime("%Y-%m-%d"))
    return value



if __name__ == "__main__":

    get_pastdays_as_list(datetime.datetime.now())
