
import os
import json
from flask import Flask
from flask import jsonify
import utilityFunctions
app = Flask(__name__)

@app.route('/testHelloWorld')
def testHelloWorld():
    return utilityFunctions.helloWorld()

@app.route('/testFibonacci')
def testFibonaci():
    return str(utilityFunctions.fibonacci())

@app.route('/testReverseSum')
def testReverseSum():
    return str(utilityFunctions.reverseSum())

@app.route('/testFileRetrival')
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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9885)



