# flows
Simple python script for generating input files for CSC 360 A2 at UVic

---
## usage
Run with defaults:
``` bash
python flows.py
```
> Creates and populate flows.txt with 10 flows, arriving within 100ms, and taking at most 1000ms to transmit.

Optionally specify output file, number of flows, and max arrival delay and max transmission time.
``` bash
python flows.py [file] [numFlows] [maxArrivalTime maxTransmissionTime]
```
## Sample output
```
$> cat flows.txt
10
1:71,38,5
2:0,407,9
3:55,181,9
4:33,632,3
5:52,121,7
6:71,15,5
7:58,750,3
8:18,57,7
9:66,978,6
10:12,739,6
```
