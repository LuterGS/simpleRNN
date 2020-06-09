from flask import Flask, render_template, request, Response
from flask_cors import CORS, cross_origin
import os
from werkzeug.utils import secure_filename
import time
import threading

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def webserver():
    # 웹서버가 실행되면서 get으로 html을 요청하면 값을 자동으로 받아오게끔 설
    app.run(host='0.0.0.0', port=80)

def get_data_everyday():
    while True:
        # 여기에 외부에서 값을 받아와 DB에 저장하고 예측하는 부분이 구현되어야함
        time.sleep(40 * 60)


"""
@app.route('/face', methods=['GET', 'POST'])
def get_pic():
    if request.method == 'POST':
        # print(request.files)
        file = request.files['file']
        file_name = secure_filename(file.filename)
        # print(app.instance_path)
        file_path = os.path.join('/home/lutergs/FaceServer', 'Pic', file_name)
        file.save(file_path)
        print(file_path)

        result = get_pic_result(file_path)
        print(request.files, result)

        desl = 'rm -rf ' + file_path
        os.system(desl)
        return result
    if request.method == 'GET':
        return render_template('index.html')
"""


if __name__ == '__main__':

    web_server = threading.Thread(target=webserver)
    everyday_loop = threading.Thread(target=get_data_everyday)

    web_server.start()
    everyday_loop.start()
