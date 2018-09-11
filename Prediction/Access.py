#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()

server.retrieve({
    'stream': "oper",
    'levtype': "sfc",
    'param': "aod550",
    'dataset': "cams_nrealtime",
    'step': "0/3/6/9/12/15/18/21/24/27/30/33/36/39/42/45/48/51/54/57/60/63/66/69/72/75/78/81/84/87/90/93/96/99/102/105/108/111/114/117/120",
    'expver': "0001",
    'time': "03",
    'date': "1997-06-01/to/2016-06-11",
    'type': "fc",
    'class': "mc",
    'target': "cams_nrealtime.grib"
})