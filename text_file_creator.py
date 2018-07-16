#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 13:24:57 2018

@author: a_santos
"""

import numpy as np
import time

def TX_RX():
    a = np.random.randint(0, 2, 1)
    if a == 0:
        TX_RX_value = 'TX'
    else:
        TX_RX_value = 'RX'
    return(TX_RX_value)

file_construction  = ''

i = 100
while i:
    t = time.time()
    file_construction = file_construction + \
                        '{0:.6f}'.format(t) + '\t' \
                        'ID_' + hex(np.random.randint(16, 256, 1)[0]).upper()[2:] + '\t' + \
                        TX_RX() + '\t' + \
                        hex(np.random.randint(16, 256, 1)[0]).upper()[2:] + ' ' + \
                        hex(np.random.randint(16, 256, 1)[0]).upper()[2:] + ' ' + \
                        hex(np.random.randint(16, 256, 1)[0]).upper()[2:] + ' ' + \
                        hex(np.random.randint(16, 256, 1)[0]).upper()[2:] + ' ' + \
                        hex(np.random.randint(16, 256, 1)[0]).upper()[2:] + ' ' + \
                        hex(np.random.randint(16, 256, 1)[0]).upper()[2:] + ' ' + \
                        hex(np.random.randint(16, 256, 1)[0]).upper()[2:] + ' ' + \
                        hex(np.random.randint(16, 256, 1)[0]).upper()[2:] + ' ' + \
                        '\n'
    i -= 1

#%%
text_file = open("log_example.asc", "w")
text_file.write(file_construction)
text_file.close()