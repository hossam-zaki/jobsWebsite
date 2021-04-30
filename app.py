from os import environ

from flask import Flask, redirect, render_template, request
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#app.config['SERVER_NAME'] = 'hiredhalal.com'
mongoURI = 'mongodb+srv://dbuser:dbpass@cluster0.5pwks.mongodb.net/jobsdb?retryWrites=true&w=majority'
client = MongoClient(mongoURI, connectTimeoutMS=30000)

db = client.get_database('jobsdb')
coll = db['jobs']
cursor = coll.find({})

for doc in cursor:
    print(doc)


@app.route('/')
def index():
    print("Hello Mars")
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
