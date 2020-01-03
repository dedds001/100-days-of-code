#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:42:06 2020

@author: deborahsilva

This simple function looks inside a directory with timestamped files, 
keeps the most recent and moves the rest to an archive folder.
"""
import argparse
import sys 
import os 
from os import listdir
from os.path import isfile, join

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filepath', type =str, default = 'files/',
                        help ='What is the filepath of the directory?')
    parser.add_argument('--filepath2', type =str, default = 'files_archive/',
                        help ='What is the filepath of the new directory?')
    args = parser.parse_args()
    sys.stdout.write(str(add_asterisk(args)))
    
 

   
def add_asterisk(args):
    onlyfiles = [f for f in listdir(args.filepath) if isfile(join(args.filepath, f))]
    onlyfiles.sort(reverse = True)
    if len(onlyfiles) > 1:
        tomove = onlyfiles[1:]
        for x in tomove:
            os.replace(args.filepath+x, args.filepath2+x )
        a = str(len(tomove))+ ' files moved.'
    else:
        a = '0 files moved.'
    return(print(a))
        
   

if __name__ == '__main__':
    main()


