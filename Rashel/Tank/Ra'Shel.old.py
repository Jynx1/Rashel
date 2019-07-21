## Text menu in Python

import List
import os

os.system('python List.py')

def print_menu():
    print 30 * "-" , "Ra' Shel Menu'" , 30 * "-"
    print "1. Menu Online 1"
    print "2. Menu List 2"
    print "3. Menu Option 3"
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
        print "Menu 1 Online"
        ## You can add your code or functions here
    if choice==2:
        print "Menu 2 show List"
        File_object = open("List.py", "r")
        #print file.read()
         ## You can add your code or functions here
    if choice==3:
        print "Menu 3 has been selected"
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