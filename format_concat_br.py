#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 18:03:43 2020

@author: deborahsilva
"""


import os 
from os import listdir
from os.path import isfile, join
import pandas as pd


v_stack = pd.DataFrame(columns =['YEAR', 'MONTH', 'TEMPERATURE', 'CITY'])
filepath = "temperature-timeseries-for-some-brazilian-cities/"
onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]
onlyfiles = [f for f in onlyfiles if 'station' in f]  
for x in onlyfiles:
    city = x.split('.', 1)[0].split('_', 1)[1]    
    df = pd.read_csv(filepath+x)
    df = pd.melt(df, id_vars=['YEAR'], value_vars=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP',
       'OCT', 'NOV', 'DEC', 'D-J-F', 'M-A-M', 'J-J-A', 'S-O-N', 'metANN'], var_name='MONTH', value_name='TEMPERATURE')
    df['CITY'] = city
    v_stack = pd.concat([v_stack, df], axis=0)
v_stack.to_csv(filepath+"all_cities_temps.csv")


