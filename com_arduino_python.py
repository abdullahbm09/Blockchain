# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 13:25:46 2017

@author: glassbox
"""

"""Module importation"""
import serial

import time

"""Opening of the serial port"""
try:
    arduino = serial.Serial("/dev/ttyACM0" ,timeout=1)
except:
    print('Please check the port')

"""Initialising variables""" 
data_raw=[]
count=0

"""Receiving data and storing it in a list"""
while True:
    data_raw = arduino.readline()
    print(data_raw)
    time.sleep(2)
#rawdata.append(str(arduino.readline()))
   # count+=1
    #print(rawdata)
'''
def clean(L):#L is a list
    newl=[]#initialising the new list
    for i in range(len(L)):
        temp=L[i][2:]
        newl.append(temp[:-5])
    return newl
    
cleandata=clean(rawdata)

def write(L):
    file=open("data.txt",mode='w')
    for i in range(len(L)):
        file.write(L[i]+'\n')
    file.close()

write(cleandata)
'''
