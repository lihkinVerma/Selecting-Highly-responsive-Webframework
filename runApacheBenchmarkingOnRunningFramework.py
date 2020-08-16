
import os
import sys

cmd = "ab -n {} -c {} localhost:{}/{} > {}Res{}_{}_{}_{}.txt"
port = sys.argv[1]
framework = sys.argv[2]
testURL = sys.argv[3]

for req in [10000]:
    for con in [20]:
        for i in range(1,6):
            print("Running framework benchmarking %s times"%str(i))
            now = cmd.format(req, con, port, testURL, framework, testURL, req, con, i)
            os.system(now)
