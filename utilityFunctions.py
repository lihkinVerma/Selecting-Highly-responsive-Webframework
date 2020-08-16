
import pymongo, gridfs
import io, glob as g,logging
import binascii
from bson import ObjectId

# local DB credentials
MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_DB = "mongotest"

con = pymongo.MongoClient(MONGO_HOST+':'+str(MONGO_PORT))
db = con[MONGO_DB]
fs = gridfs.GridFS(db)

def retrieveModelByNameAndVersion(modelName, modelVersion):
    try:
        return fs.find_one({'modelName':modelName, 'modelVersion': modelVersion}).read()
    except Exception as e:
        print("Model not retrieved")

def helloWorld():
	return "Hello World"

def fibonacci(n = 100):
    fib = [1, 1]
    for i in range(n):
        fibi = fib[-1] + fib[-2]
        fib.append(fibi)
    return fib[-1]

def reverseSum(n = 1000):
    summation = 0
    for i in range(1, n):
        summation += 1/i
    return summation
	
