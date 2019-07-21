#!/usr/bin/python
# Rashel.py - Eve.Profile.py
# Authors:  Jraglin
# Version: V1.02-21-17.01.30A
# Last stable: Rashel.old.py
#---------------------------------------------------------------------
## Text menu in Python

#import System.Menu
import os
os.system('python System.Menu.py')


def print_menu():
    print 30 * "-" , "Ra' Shel Menu'" , 30 * "-"
    print "1. Menu Scan 1"
    print "2. Menu System 2"
    print "3. Menu Security 3"
    print "4. Menu Option 4"
    print "5. Exit"
    print 67 * "-"
## Your menu design here

loop=True
while loop:
## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
    if choice==1:
        print "Menu 1 Scan"
        ## You can add your code or functions here
	

    if choice==2:
        # print "Menu 2 Show Data"
        ## You can add your code or functions here
        File = open("System.Menu.py", "r")
        #print file.read()
    if choice==3:
        print "Menu 3 Security"
        ## You can add your code or functions here
    if choice==4:
        print "Menu 4 has been selected"
        ## You can add your code or functions here
    if choice==5:
        print "Menu 5 has been selected"
        ## You can add your code or functions here
        loop=False
        # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
