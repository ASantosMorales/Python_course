#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 20:52:13 2018

@author: a_santos
"""

with open('log_example.asc') as f:
    lines = f.readlines()

file_construction = ''
for line in lines:
    if 'RX' in line:
        file_construction = file_construction + line
        print(line[:-1])

#text_file = open("log_example_modificated.asc", "w")
#text_file.write(file_construction)
#text_file.close()