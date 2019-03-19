#!/usr/bin/python

#############################################################
#|
#|  Obviously the code below is incorrect and will not function correctly.
#|  Try to see what the issue may be. Thought I'm listing some simple commands for Python3, try going on
#|  https://www.geeksforgeeks.org/python-3-basics/ 
#|  to learn more
#|
#|  How to import stuff:
#|  import <module>
#|
#|  How to create a function:
#|  def <name>():
#|     <code here>
#|
#|  How to print something:
#|  print("<type stuff here>")
#|
#|  How to commentate:
#|  # <Commentary>
#|
#############################################################
#| 
#| Please fix, commentate, and edit any code under the line below!
#| 
#############################################################

import os
import sys
import platform
import time


# The function uses the "os" module to get a result of either, linux1, linux2, darwin, or win32
def get_platform():
    platforms = {
        'linux1' : 'Linux', #if the platform gets linux1, call it "Linux"
        'linux2' : 'Linux', #if the platform gets linux2, call it "Linux"
        'darwin' : 'Mac OS X', #if the platform gets dawrin, call it "Mac OS X"
        'win32' : 'Windows' #  if the platform gets win32, call it "Windows"
    }


print("Welcome! Here's your system informatio! /n")

print("Your Local Time Zone: " + time.time()) # <Local time zone>

print("Your platform         " + get_platform()) # <Gets platform>

print("Release Version       " + platform.release()) # <Gives the version of platform>

print("System:               " + platform.system()) # <Gives system running>

print("Machine:              " + platform.machine()) # <Gives the machine>


