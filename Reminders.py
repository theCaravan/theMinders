from datetime import *
from time import *

def getRemindersFromFile(location=""):
        read_into = open(location, "r")

        done_reading = False
        flags = ""
        categories = []
        reminder_parts = []
        reminders = []
        
        while not done_reading:
            nxt_line = read_into.readline()

            if flags != "":
                if flags == "C":
                   categories = nxt_line.split(" , ")

                elif flags == "P":                   
                   reminder_parts = nxt_line.split(" , ")
                   flags = "R"
                   continue

                elif flags == "R":
                   if nxt_line != "-END-OF-REMINDERS-\n":
                       reminders.append(nxt_line.split(" , "))
                       flags = "R"
                       continue
                           
                elif flags == "EOF":
                   if nxt_line == "":
                        output = []
                        output.append(categories)
                        output.append(reminder_parts)
                        output.append(reminders)
                       
                        return output
                
                flags = ""
                continue

                
            elif nxt_line != "":
                if nxt_line == "Categories:\n":
                    flags = "C"
                    continue

                elif nxt_line == "Reminders:\n":
                    flags = "P"
                    continue
                
            else:
                flags = "EOF"
                continue

def printLine(length=0, character=""):
    count = 1
    while count < length:
        print(character, end="")
        count += 1

##def padding(array=[], padding=""):
##    len_line = len(padding.lstrip("")) - 1
##    print(padding.lstrip(), end="")
##    for arr in array:
##        arr = arr.replace("\n", "")
##        len_line += len(arr) + len(padding)
##        print(arr, end=padding)
##    print()
##    return len_line

print("The time is: " + str(localtime()[3]) + ":" + str(localtime()[4]))

into = getRemindersFromFile("/home/sb5060tx/Documents/myPrograms/Caravan Projects/Reminders.txt")

categories = into[0]
reminder_parts = into[1]
reminders = into[2]
len_line = 3

print("\nYou have " + str(len(reminders)) + " reminders: \n")

due_today = []

for reminder in reminders:
    if reminder[5].isalpha() != True:
        deadline = (reminder[5].replace(":", "-")).replace(" ","-").split("-")

        ## You have the deadline as an array, now compare it with localtime[] so as to determine which deserves more priority
    
    else:
        deadline = reminder[5]
        ## Presets:
        ##          1- Salah Time
        ##          2- Arrival to XXX Location
        ##          3- Before Bed and After Bed
        

'''
Sort it so as to say like this, even on two or more columns if possible:


SALAH


DUE TODAY:
    ----------- XXX time LEFT
    -----------
    -----------

DUE THIS WEEK
    ----------- Due in X Days (XXX time)
    -----------

DUE NEXT WEEK
    -----------
    -----------

HOUSEHOLD CHORES




    
>>> New Reminder
>>> Done NAME
>>> Postpone NAME to DATE at TIME
>>> Move up NAME to DATE at TIME
>>> Change priority NAME to PRIORITY
>>> Delete NAME
>>> Add Note NAME = fjdskfldajslajgdsjlajgldgljflgjflgjlalj
>>> Exit    
>>> Open FILE    

''' 


cmd = input("REMINDERS >>> ")
