import datetime
import os
import threading
import time
from flask import Flask, render_template

import WorkAI

folder_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, template_folder=folder_path + '/template')
worker = WorkAI.Worker()

@app.route('/')
def index():
    # return render_template('index.html', test=worker.result)
    return render_template('index.html', value=worker.result, date=worker.cur_time.strftime("%Y년 %m월 %d일"))


def webserver():
    app.run(host='0.0.0.0', port=80)

def get_data_everyday():
    while True:
        # 여기에 외부에서 값을 받아와 DB에 저장하고 예측하는 부분이 구현되어야함
        cur_time = datetime.datetime.now()
        if int(cur_time.hour) == 17:
            worker.work_oneday()
            worker.cur_time = datetime.datetime.now() + datetime.timedelta(days=1)
            time.sleep(3720)
        time.sleep(300)

if __name__ == '__main__':
    # app.run()
    web_server = threading.Thread(target=webserver)
    everyday_loop = threading.Thread(target=get_data_everyday)

    web_server.start()
    everyday_loop.start()
