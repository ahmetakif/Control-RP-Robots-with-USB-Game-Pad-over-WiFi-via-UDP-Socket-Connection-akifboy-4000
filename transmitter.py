#This is the AKIBOY_ROBOT_CONTROLLER CODE

#WELCOME MESSAGES
print("----------------------------")
print("Welcome")
print("This is the AKIBOY_ROBOT_CONTROLLER CODE")
print("----------------------------")

#UDP
import socket

UDP_IP = "192.168.1.15" #IP of the robot - same on the robot
UDP_PORT = 5005 # Port - also same on the robot

#import evdev
from evdev import InputDevice, categorize, ecodes

import time

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#button code variables (change to suit your device)
Btn1 = 288
Btn2 = 289
Btn3 = 290
Btn4 = 291

start = 297
select = 296

lTrig = 294
rTrig = 295

lanalogbtn = 298
ranalogbtn = 299

atime = 0.2

#prints out device info at start
print(gamepad)
print("----------------------------")
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("----------------------------")

#Some other UDP Things
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

message = b"Hello, World!"

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == Btn1:
                print("1_one")
                message = b"1_one"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == Btn2:
                print("1_two")
                message = b"1_two"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == Btn3:
                print("1_three")
                message = b"1_three"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == Btn4:
                print("1_four")
                message = b"1_four"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == start:
                print("1_start")
                message = b"1_start"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == select:
                print("1_select")
                message = b"1_select"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == lTrig:
                print("1_left_bumper")
                message = b"1_left_bumper"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == rTrig:
                print("1_right_bumper")
                message = b"1_right_bumper"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == lanalogbtn:
                print("1_left_analog_button")
                message = b"1_left_analog_button"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == ranalogbtn:
                print("1_right_analog_button")
                message = b"1_right_analog_button"
                sock.sendto(message, (UDP_IP, UDP_PORT))
        if event.value == 0:
            if event.code == Btn1:
                print("0_one")
                message = b"0_one"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == Btn2:
                print("0_two")
                message = b"0_two"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == Btn3:
                print("0_three")
                message = b"0_three"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == Btn4:
                print("0_four")
                message = b"0_four"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == start:
                print("0_start")
                message = b"0_start"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == select:
                print("0_select")
                message = b"0_select"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == lTrig:
                print("0_left_bumper")
                message = b"0_left_bumper"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == rTrig:
                print("0_right_bumper")
                message = b"0_right_bumper"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == lanalogbtn:
                print("0_left_analog_button")
                message = b"0_left_analog_button"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.code == ranalogbtn:
                print("0_right_analog_button")
                message = b"0_right_analog_button"
                sock.sendto(message, (UDP_IP, UDP_PORT))
    if event.type == ecodes.EV_ABS:
        if event.code == 1:
            if event.value > 200:
                print("ldown")
                time.sleep(atime)
                message = b"ldown"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.value < 50:
                print("lup")
                time.sleep(atime)
                message = b"lup"
                sock.sendto(message, (UDP_IP, UDP_PORT))
        if event.code == 2:
            if event.value > 200:
                print("lright")
                time.sleep(atime)
                message = b"lright"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.value < 50:
                print("lleft")
                time.sleep(atime)
                message = b"lleft"
                sock.sendto(message, (UDP_IP, UDP_PORT))
        if event.code == 3:
            if event.value > 200:
                print("rright")
                time.sleep(atime)
                message = b"rright"
                sock.sendto(message, (UDP_IP, UDP_PORT))
            elif event.value < 50:
                print("rleft")
                time.sleep(atime)
                message = b"rleft"
                sock.sendto(message, (UDP_IP, UDP_PORT))
