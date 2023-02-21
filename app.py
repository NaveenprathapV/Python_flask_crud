from flask import Flask, request, json 
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_pyfile('config.py')
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
    return 'Student added successfully'

@app.route('/student/<name>', methods = ['PUT'])
def updateStudents(name):
    print(name)
    # id = request.args.get('id')
    data = json.loads(request.data)
    studentData = mongo.db.students.update_one({ 'name': name }, { "$set": data })
    return "Student updated successfully"
    

@app.route('/student/delete/<id>', methods = ['DELETE'])
def deleteStudents(id):
    # id = request.args.get('id')
    deleteQuery= {"_id": ObjectId(id)}
    studentData = mongo.db.students.delete_one(deleteQuery)
    return "Student deleted successfully"
    
    
if __name__ == '__main__':
    app.run()