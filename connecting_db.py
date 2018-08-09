from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'database1'
app.config['MONGO_URI'] = 'mongodb://maryam:maryam22@ds111492.mlab.com:11492/database1'
mongo = PyMongo(app)


@app.route("/")
def index():
    students = []
    records = mongo.db.student.find({'user': 'qasim'})
    for user in records:
        students.append({'name': user['user'], \
                         'password': user['pass']})

    return jsonify({'SaylaniStudents': students})


@app.route("/add")
def add():
    add = mongo.db.student.insert({'name': 'kashan'})
    return "Successfully add"


app.run(debug=True)