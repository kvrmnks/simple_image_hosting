from DataBase import LDataBase
from flask import Flask
import flask
from flask import request
import random

host = 'localhost'
port = 3306
name = 'root'
password = ''
database_name = ''

test = LDataBase(
    host,
    port,
    name,
    password,
    database_name,
)
app = Flask(__name__)


@app.route('/')
def readMe():
    return flask.render_template('index.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == "POST":
        print(request.headers)
        file = request.files['file']

        if file is None:
            return flask.render_template('upload.html')

        data = file.read()
        name = ""
        for i in range(10):
            name += str(random.randrange(0, 10))

        global test
        test.insertPics(name, file.filename, data)
        return "/upload/" + name

    return flask.render_template('upload.html')


@app.route('/upload/<id>')
def uploadId(id):
    data = test.getPicsById(id)
    name = data[0]['name'].split(".")
    name = name[len(name) - 1]
    return flask.Response(data[0]['data'], mimetype='image/' + name)


@app.route('/about', methods=['POST', 'GET'])
def readMe2():
    if request.method == 'POST':
        global test
        test.clearTables()
        return "跑路成功"
    return flask.render_template('about.html')


@app.route('/list')
def showList():
    global test
    data = test.getList()
    data = list(data)
    data.sort(key=lambda x: x['time'])
    return flask.render_template('list.html', data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7000)
