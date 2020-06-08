from flask import Flask, render_template, request, Response
from flask_cors import CORS, cross_origin
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


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
    app.run(host='0.0.0.0', port=80)
