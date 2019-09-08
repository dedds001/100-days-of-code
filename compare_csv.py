#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:17:47 2019

@author: deborahedds
"""


import argparse
import sys 
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filepath1', type =str, default = 'test1.csv',
                        help ='What is the first file location?')
    parser.add_argument('--filepath2', type =str, default ='test2.csv', 
                        help ='What is the second file location?')
    parser.add_argument('--operation', type =str, default ='shared', 
                        help ='What operation? (first_file_only, shared, second_file_only, \
                                                num_first_only, num_shared, num_second_only')
    parser.add_argument('--column', type =str, default ='acct_id', 
                        help ='What column to compare?')
    args = parser.parse_args()
    sys.stdout.write(str(compare_csv(args)))
    
   
def compare_csv(args):
    df1 = pd.read_csv(args.filepath1)
    df2 = pd.read_csv(args.filepath2)
    if args.operation == 'first_file_only':
        newdf = df1.merge(df2, indicator='i', how='outer', on=args.column).query('i == "left_only"').drop('i', 1)
        list1 = newdf[args.column].tolist()
        return print(args.column, ' from first file not present in second file: ', list1)
    elif args.operation == 'num_first_only':
        newdf = df1.merge(df2, indicator='i', how='outer', on=args.column).query('i == "left_only"').drop('i', 1)
        list1 = newdf[args.column].count()
        return print(args.column, ' from first file not present in second file: ', list1)
    elif args.operation =='shared':
        newdf = df1.merge(df2, how='inner', on=args.column)
        list1 = newdf[args.column].tolist()
        return print(args.column, 'shared by both files: ', list1)
    elif args.operation =='num_shared':
        newdf = df1.merge(df2, how='inner', on=args.column)
        list1 = newdf[args.column].count()
        return print(args.column, 'shared by both files: ', list1)
    elif args.operation =='second_file_only':
        newdf = df1.merge(df2, indicator='i', how='outer', on=args.column).query('i == "right_only"').drop('i', 1)
        list1 = newdf[args.column].tolist()
        return print(args.column, ' from second file not present in first file: ', list1)
    elif args.operation =='num_second_only':
        newdf = df1.merge(df2, indicator='i', how='outer', on=args.column).query('i == "right_only"').drop('i', 1)
        list1 = newdf[args.column].count()
        return print(args.column, ' from second file not present in first file: ', list1)
    else:
        return print('not a valid operation')

if __name__ == '__main__':
    main()

