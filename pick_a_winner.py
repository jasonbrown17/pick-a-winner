#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jason Brown'
__email__  = 'jason@jasonbrown.us'
__date__   = '20201009'

import random, csv, sys

'''Produce randomized seed'''
seedvalue = random.randrange(sys.maxsize)
random.seed(seedvalue)

'''Ask user for file name'''
winners = input('File name: ')

'''Check if file exists'''
try:
    with open(winners, 'rt')as f:
        name = list(csv.reader(f))
    f.close()
except FileNotFoundError:
    print('File not found')

'''Provide a randomized seed value for shuffling names'''
try:
    random.Random(seedvalue).shuffle(name)
    print('\nThe winner is: ')
    print(name[0])
except NameError:
    print('There was a problem reading the file\n')