version = "PRE-ALPHA Build 9"
print("The Minders -- by The Caravan -- " + version)
from datetime import *
from time import *

categories = ["Big Projects", "Chores", "Islam", "Studying",
              "Important", "Planning"]

reminder_parts = ["Done", "Category", "Name", "Occurrance",
                  "Date Assigned", "Due Date", "Submission Method",
                  "Additional Notes"]

reminders = [
                ["No", "0", "Physics Lab Report", "NULL", "2016,4,1",
                  "2016,4,8,16,0,0", "Paper", "Turn in Williamson Hall 150"],

                ["No", "0", "Arch Lab", "NULL", "2016,3,28", "2016,4,13,11,55,0",
                 "Moodle", "See Num 8 Page 12"]
            ]


def printLine(length=0, character="", lineBreakAtEnd=True):
    count = 1
    pr = ""
    while count < length:
        pr += character
        count += 1

    if lineBreakAtEnd == True:
        print(pr+"\n")

    else:
        print(pr)

def secondsToDateTime(timeDelta=0.0):

    delta = (timeDelta - datetime.now()).total_seconds()

    yr = delta / (86400*365.25)
    mn = (yr - int(yr)) * 12
    dy = (mn - int(mn)) * 30.4375
    hr = (dy - int(dy)) * 24
    mi = (hr - int(hr)) * 60
    sc = (mi - int(mi)) * 60

    return datetime(int(yr), int(mn), int(dy), int(hr), int(mi), int(sc))

while True:
    print("\nToday is " + str(date.today().month) + "/" + str(date.today().day) + "/" + str(date.today().year))
    print("\nThe time is: " + str(datetime.now().hour) + ":" + str(datetime.now().minute))

    printLine(88, "-", True)
    
    len_line = 3

    print("\nYou have " + str(len(reminders)) + " reminders: \n")

    due_sort = []

    for reminder in reminders:
        if reminder[5].isalpha() != True:
            deadline = (reminder[5]).split(",")
            for part in deadline:
                deadline[deadline.index(part)] = int(part)
            
            deadline = datetime(deadline[0], deadline[1], deadline[2], deadline[3], deadline[4], deadline[5])

            delta = secondsToDateTime((deadline - datetime.now()).total_seconds())
            
            if delta < 0:
                print("WARNING: Deadline for this has passed")
                due_sort.append(reminder)

                
                    
        
        else:
            deadline = reminder[5]
            ## Presets:
            ##          1- Salah Time
            ##          2- Arrival to XXX Location
            ##          3- Before Bed and After Bed 
        
    while True:
        cmd = input("\nREMINDERS >>> ")

        if cmd in ["New", "new", "n", "N"]:
            newReminder = []
            for reminder_part in reminder_parts:
                newReminder.append(input("\t" + str(reminder_part) + ": "))

        elif cmd in ["Exit", "exit", "X", "x"]:
            if input("Are you sure you want to exit? (Y/n): ") != "n":
                exit(0)
                
        elif cmd in ["", " "]:
            continue
                
        else:
            print("Cannot determine what '" + cmd + "' means")

    input("PAUSE")
