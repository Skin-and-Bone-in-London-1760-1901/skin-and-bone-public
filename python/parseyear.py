#!/usr/bin/python3

import datetime

def parseyear(ds):

    if isinstance(ds, str):

        parts = ds.split('/')

        return parts[-1]

    elif isinstance(ds, datetime.datetime):
 
        return ds.year

