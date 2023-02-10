from flask import Flask, request, json 
from bson.objectid import ObjectId
from pymongo import MongoClient

app = Flask(__name__)

def createConnection():
    connection = MongoClient("mongodb://localhost:27017")
    db = connection.flask_db
    return db

@app.route('/students', methods = ['GET'])
def getStudents():
    db = createConnection()
    studentData = list(db.students.find({}))
    # return studentData
    # return json.dumps(studentData)
    # return jsonify(list(studentData))
    return object.__str__(studentData)

@app.route('/student', methods = ['POST'])
def createStudents():
    db = createConnection()
    data = json.loads(request.data)
    studentData = db.students.insert_one(data)
    return object.__str__(studentData)

@app.route('/student/:id', methods = ['PUT'])
def updateStudents():
    db = createConnection()
    id = request.args.get('id')
    data = json.loads(request.data)
    print(data)
    studentData = db.students.update_one({ '_id': ObjectId(id) }, { "$set": data })
    return "hi"

@app.route('/student/:id', methods = ['DELETE'])
def deleteStudents():
    db = createConnection()
    id = request.args.get('id')
    deleteQuery= {"_id": ObjectId(id)}
    
if __name__ == '__main__':
    print('enter')
    app.run(port=7777)
