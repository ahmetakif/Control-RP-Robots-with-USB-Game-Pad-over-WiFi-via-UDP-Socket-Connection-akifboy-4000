# This is the code for the DUMMY_ROBOT controlled by the AKIFBOY via UDP

#WELCOME MESSAGES
print("----------------------------")
print("Welcome")
print("This is the code for the DUMMY_ROBOT controlled by the AKIFBOY via UDP")
print("----------------------------")

#UDP
import socket

UDP_IP = "192.168.1.15" #IP of the robot - same on the robot
UDP_PORT = 5005 # Port - also same on the robot

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


def helpcommands():
    print ("|-----Meanings of keyboard control commands-----|")
    print ("'w' = Goes forward")
    print ("'s' = Goes backward")
    print ("'a' = Pivot turns to the left")
    print ("'d' = Pivot turns to the right")
    print ("'q' = Turns to the left")
    print ("'e' = Turns to the right")
    print ("'akifboy' = Enter the UDP Socket Control Mode, please use the AKIFBOY to control DUMMY!")
    print ("'exit', 'quit', 'escape', 'suspense' = Quits the program")
    print (" ")

#IMPORTMENTS
import serial
#import sys
import time
#import json
import RPi.GPIO as gpio
import random


#ARDUINO SERIAL
a = serial.Serial('/dev/ttyACM0',9600)


#ARDUINO A
def forward():
    a.write('a')
def backward():
    a.write('b')
def left():
    a.write('c')
def right():
    a.write('d')
def leftp():
    a.write('e')
def rightp():
    a.write('f')
def stopp():
    a.write('g')

#MOVE FUNCTIONS
def mforward(tf):
    forward()
    tf = float(tf)
    time.sleep(tf/10)
    stopp()
def mbackward(tf):
    backward()
    tf = float(tf)
    time.sleep(tf/10)
    stopp()
def mleft(tf):
    left()
    tf = float(tf)
    time.sleep(tf/10)
    stopp()
def mright(tf):
    right()
    tf = float(tf)
    time.sleep(tf/10)
    stopp()
def mleftp(tf):
    leftp()
    tf = float(tf)
    time.sleep(tf/10)
    stopp()
def mrightp(tf):
    rightp()
    tf = float(tf)
    time.sleep(tf/10)
    stopp()

#DEBUGGING AND CONTROLLING REMOTELY
while True:
    y = raw_input("Command: ")
    if y == "w":
        print "Going forward"
        mforward(1)
    elif y == "s":
        print "Going backward"
        mbackward(1)
    elif y == "a":
        print "Turning left"
        mleftp(1)
    elif y == "d":
        print "Turning right"
        mrightp(1)
    elif y == "q":
        print "Going to the left"
        mleft(1)
    elif y == "e":
        print "Going to the right"
        mright(1)
    elif y == "exit" or y == "quit" or y == "escape" or y == "suspense":
        print "Quitting the main program, hope to see you soon -DUMMY"
        break
    elif y == "help":
        helpcommands()
    elif y == "akifboy":
        print "Entering the UDP Socket Remote Control Mode, please use the AKIFBOY to control me! Type CTRL+C to exit. -DUMMY"
        while True:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            if data == "lup":
                print "Going forward"
                mforward(1)
            elif data == "ldown":
                print "Going backward"
                mbackward(1)
            elif data == "lleft":
                print "Turning left"
                mleftp(1)
            elif data == "lright":
                print "Turning right"
                mrightp(1)
            elif data == "rleft":
                print "Going to the left"
                mleft(1)
            elif data == "rright":
                print "Going to the right"
                mright(1)
            elif data == "stop":
                print("stop")
                stopp()
            elif data == "1_right_bumper":
                print("Stop NOW!")
                stopp()
            else:
                print("UDP Socket ERROR: Unknown Message")
    else:
        print "This command does not exist please try another or check the guide above"
        stopp()
