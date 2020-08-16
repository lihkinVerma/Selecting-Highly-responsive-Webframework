
import os
import subprocess
import shutil as sh
from psutil import process_iter
from signal import SIGKILL

# Make directories to store results
try:
    os.mkdir('falconResults')
except Exception as e:
    pass

try:
    os.mkdir('fastApiResults')
except Exception as e:
    pass

try:
    os.mkdir('flaskResults')
except Exception as e:
    pass

# Command to run apache benchmarking tool
cmd = "python3 runApacheBenchmarkingOnRunningFramework.py {} {} {}"

# Urls to check AB tool results
testURLs = ['testHelloWorld', 'testFibonacci', 'testFileRetrival']

# Commands to start various frameworks
startFalcon = 'gunicorn  -b 127.0.0.1:9883 testFalcon &'
startFastApi = 'uvicorn testFastApi:app --port 9884 &'
startFlask = 'python3 testFlask.py &'

# Mapping of framework to port and cmd to start it
dictOfPortFrameworks = { 
#        'Falcon':[9883, startFalcon] , 
        'FastApi':[9884, startFastApi] , 
        'Flask':[9885, startFlask]
        }

def killProcessOnParticularPort(portNo):
    for proc in process_iter():
        try:
            for conns in proc.connections(kind='inet'):
                if conns.laddr.port == portNo:
                    proc.send_signal(SIGKILL)
                    print("-------------------kill with port no %s"%str(portNo))
        except Exception as e:
            pass

# Calling all frameworks in loop
for framework, port in dictOfPortFrameworks.items():
    cmdToStartFramework = port[1]
    port = port[0]
    #killProcessOnParticularPort(port)
    print("Giving command to system %s"%cmdToStartFramework)
    os.system(cmdToStartFramework)
    for testURL in testURLs:
        lofPre = set(os.listdir())
        now = cmd.format(port, framework, testURL)
        os.system(now)
        lofPost = set(os.listdir())
        if framework is 'Falcon':
            for filename in lofPost-lofPre:
                try:
                    sh.copy(filename, 'falconResults')
                    os.remove(filename)
                except Expception as e:
                    pass
        elif framework is 'FastApi':
            for filename in lofPost-lofPre:
                try:
                    sh.copy(filename, 'fastApiResults')
                    os.remove(filename)
                except Exception as e:
                    pass
        elif framework is 'Flask':
            for filename in lofPost-lofPre:
                try:
                    sh.copy(filename, 'flaskResults')
                    os.remove(filename)
                except Exception as e:
                    pass
    #killProcessOnParticularPort(port)
