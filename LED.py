#Program to Control LED of Arduino from Python
#Code by: Aswinth Raj, Dated: 8-9-2017
#Website: www.circuitdigest.com

import serial #Serial imported for Serial communication
import time #Required to use delay functions
 
ArduinoSerial = serial.Serial('/dev/ttyACM1', 9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

#print ArduinoSerial.readline() #read the serial data and print it as line
print ("Enter 1 to turn ON LED and 0 to turn OFF LED")

 
while 1: #Do this forever

    abcd = input() #get input from user
    #print "you entered", var #print the intput for confirmation
    
    if (abcd == '1'): #if the value is 1
        ArduinoSerial.write('1') #send 1
        print ("LED turned ON")
        time.sleep(1)
    
    if (abcd == '0'): #if the value is 0
        ArduinoSerial.write('0') #send 0
        print ("LED turned OFF")
        time.sleep(1)
