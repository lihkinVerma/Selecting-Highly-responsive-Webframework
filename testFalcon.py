
import os
import falcon
import json
import utilityFunctions

api = application = falcon.API()

class ResourceHelloWorld(object):
    def on_get(self, req, resp):
        resp.body = utilityFunctions.helloWorld()
        resp.status = falcon.HTTP_200

class ResourceFibonacci(object):
    def on_get(self, req, resp):
        resp.body = str(utilityFunctions.fibonacci())
        resp.status = falcon.HTTP_200

class ResourceReverseSum(object):
    def on_get(self, req, resp):
        resp.body = str(utilityFunctions.reverseSum())
        resp.status = falcon.HTTP_200

class ResourceFileRetrival(object):
    def on_get(self, req, resp):
        filename = 'SectionModel4Class_0PI_1Edu_2WorkEx_3Others.hdf5'
        try:
            os.remove(filename)
        except Exception as e:
            pass
        obj = utilityFunctions.retrieveModelByNameAndVersion(filename, 'v1')
        with open(filename, 'wb') as f:
            f.write(obj)
        resp.body = "Yes Saved"
        resp.status = falcon.HTTP_200

resHW = ResourceHelloWorld()
api.add_route('/testHelloWorld', resHW)

resFb = ResourceFibonacci()
api.add_route('/testFibonacci', resFb)

resRS = ResourceReverseSum()
api.add_route('/testReverseSum', resRS)

resFR = ResourceFileRetrival()
api.add_route('/testFileRetrival', resFR)
