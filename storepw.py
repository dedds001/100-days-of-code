#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:06:46 2019

@author: deborahedds
"""


import argparse
import sys 
import pandas as pd
import random
import string

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--account', type =str, default = 'email',
                        help ='What is the account?')
    args = parser.parse_args()
    sys.stdout.write(str(pword(args)))
    
 

def split_str(s):
    return [x for x in s]

def pword(args):   
    df = pd.read_csv('test2.csv')
    l = df['account'].tolist()
    if args.account in l:
        return print("Password is :", df.loc[df['account']==args.account, 'password'].iloc[0])
    else:      
        y = input("Account is not in list.  Would you like to create password?  ")
        if y.upper() =='YES':
            z=input("Do you want to generate a random password? ")
            if z.upper() == 'YES':
                l = split_str(string.ascii_lowercase)
                u = split_str(string.ascii_uppercase)
                n ='1234567890'
                n = split_str(n)
                c = '!@#$%^&*()_'
                c=split_str(c)
                a = l + u + n + c
                newlist = random.sample(l, 3) + random.sample(u, 3) + random.sample(n, 1) + random.sample(c, 1) + random.sample(a, (random.randint(0, 3)))
                random.shuffle(newlist)
                p =''.join(newlist)
                df.loc[len(df)] = [args.account, p]
                df.to_csv('test2.csv', index = False)
                return print('Password for new account is now ', p)
            else:
                x = input("Please give a password for new account")
                df.loc[len(df)] = [args.account, x]
                df.to_csv('test2.csv', index = False)
                return print('password added')
        else:
            return print('Account not added to list')

   

if __name__ == '__main__':
    main()





