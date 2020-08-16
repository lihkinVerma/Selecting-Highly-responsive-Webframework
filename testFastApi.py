
import os
from fastapi import FastAPI
import utilityFunctions

app = FastAPI()

@app.get("/testHelloWorld")
def testHelloWorld():
    return utilityFunctions.helloWorld()

@app.get('/testFibonacci')
def testFibonaci():
    return str(utilityFunctions.fibonacci())

@app.get('/testReverseSum')
def testReverseSum():
    return str(utilityFunctions.reverseSum())

@app.get('/testFileRetrival')
def testFileRetrival():
    try:
        filename = 'SectionModel4Class_0PI_1Edu_2WorkEx_3Others.hdf5'
        try:
            os.remove(filename)
        except Exception as e:
            pass
        obj = utilityFunctions.retrieveModelByNameAndVersion(filename, 'v1')
        with open(filename, 'wb') as f:
            f.write(obj)
        return "Yes Saved"
    except Exception as e:
        print("File not saved on path")
