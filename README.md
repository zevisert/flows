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

