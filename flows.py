"""
Used to create flows for CSC 360 assignment 2.

Zev Isert - Fall 2016
"""

import sys
import random
import os

"""
Used as command line input
"""
def main():
    # flows usage:
    # flows.py
    # flows.py file.txt
    # flows.py file.txt 10
    # flows.py file.txt 100 100 1000
    
    numArgs = len(sys.argv) - 1
    possibleArgLens = [0, 1, 2, 4]
    inputOk = False
    for l in possibleArgLens:
        if l == numArgs:
            inputOk = True
            break

    if not inputOk:
        usage()
        return

    file = sys.argv[1] if numArgs == 1 else "flows.txt"
    try:
        size = int(sys.argv[2]) if numArgs == 2 else 10
        maxArrivalTime = int(sys.argv[3]) if numArgs == 4 else 100
        maxTransmissionTime = int(sys.argv[4]) if numArgs == 4 else 1000
    except ValueError:
        usage()
        return

    flows = flow(size, maxArrivalTime, maxTransmissionTime)

    with open(file, "w") as output:
        output.write("%d\n" % (len(flows)))
        for k, v in flows.iteritems():
            output.write("%d:%d,%d,%d\n" % (k, v["arrival"], v["transmission"], v["priority"]))

"""
Create a flow of the specified size
"""
def flow(size, maxArrivalTime, maxTransmissionTime):
    flows = {}
    for i in range(1, size + 1):
        flows[i] = {
            "id": i,
            "priority": random.randint(1, 10),
            "arrival": random.randint(0, maxArrivalTime),
            "transmission": random.randint(1, maxTransmissionTime)
        }
    return flows

"""
Print script usage
"""
def usage():
    print "Expected args: outputFile [size] [maxArrivalTime, maxTransmissionTime]"

if __name__ == '__main__':
    main()
