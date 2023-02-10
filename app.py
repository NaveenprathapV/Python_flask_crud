from flask import Flask, request, json 
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from dotenv import load_dotenv 
import os

app = Flask(__name__)
load_dotenv()
app.config ['MONGO_URI']= os.environ.get('MONGO_URI')
mongo = PyMongo(app)

# def createConnection():
#     connection = MongoClient("mongodb://localhost:27017")
#     db = connection.flask_db
#     return db

@app.route('/students', methods = ['GET'])
def getStudents():
    studentData = list(mongo.db.students.find({}))
    return object.__str__(studentData)

@app.route('/student', methods = ['POST'])
def createStudents():
    data = json.loads(request.data)
    studentData = mongo.db.students.insert_one(data)
    return object.__str__(studentData)

@app.route('/student/:id', methods = ['PUT'])
def updateStudents():
    id = request.args.get('id')
    data = json.loads(request.data)
    print(data)
    studentData = mongo.db.students.update_one({ '_id': ObjectId(id) }, { "$set": data })
    return "hi"

@app.route('/student/:id', methods = ['DELETE'])
def deleteStudents():
    id = request.args.get('id')
    deleteQuery= {"_id": ObjectId(id)}
    
if __name__ == '__main__':
    print('enter')
    app.run(port=7777)
