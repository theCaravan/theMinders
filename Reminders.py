version = "ALPHA Build 400"
print("\nThe Minders -- by The Caravan -- " + version)
from datetime import *
from time import *

## PLANS ##
'''

Import and Export from Reminders File

    - Open new file
    - Save current state to file
    - Determine validity of file so as to determine whether to read or not

Auto Refresh (interval like 5 seconds)

    - Make it an option to configure

REMINDERS >>>
    "chk", "check" "done" "c"                    Check off completed tasks
    "add note" "+n"                              Add "additional notes"
    "cp" "change priority" "priority"            Change priority
    "pp" "mv" "postpone" "move up"               Postpone and move up
    "cn" "change name" "name"                    Change name
    "co" "change occurance" "occurance"          Change occurance
    "ss" "set settings" "options" "settings"     Set settings
    "csm" "submission method" "change..."        Change submission method
    "ls" "list commands" "list" "cmd" "commands" List Commands

Find way to accomodate daily tasks like Prayer and Chores

Find way to deal with NULL both in task creation and reading reminders

Find way so that "TODAY" is an option for date assigned

Find way to that "ASAP" is valid on due date

'''
###########

reminder_parts = ["Done", "Priority", "Name", "Occurrance",
                  "Date Assigned", "Due Date", "Submission Method",
                  "Additional Notes"]

reminders = [
                ["No", "High", "Physics Lab Report", "NULL", "2016,4,1,0,0,0",
                  "2016,4,8,16,0,0", "Paper", "Turn in Williamson Hall 150"],

                ["No", "High", "Arch Lab", "NULL", "2016,3,28,0,0,0", "2016,4,13,23,55,0",
                 "Moodle", "See Num 8 Page 12"],

                ["Yes", "High", "Physics Quiz", "NULL", "2016,4,1,0,0,0",
                 "2016,4,1,13,25,0", "Study", "Chapters 5 and 6"]
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

def dateTimeDiff(datetimeVal1="now", datetimeVal2="now"):

    if datetimeVal1 == "now":
        datetimeVal1 = datetime.now()

    if datetimeVal2 == "now":
        datetimeVal2 = datetime.now()

    timeDelta = (datetimeVal2 - datetimeVal1).total_seconds()    

    yr = timeDelta / (86400*365.25)
    mn = (yr - int(yr)) * 12
    dy = (mn - int(mn)) * 30.4375
    hr = (dy - int(dy)) * 24
    mi = (hr - int(hr)) * 60
    sc = (mi - int(mi)) * 60

    return [int(yr), int(mn), int(dy), int(hr), int(mi), int(sc)]

def lsToStr(ls=[],formatting=["--","--","--","--","--","--"]):
    f = formatting
    out = ""

    for l in ls:
        ind = ls.index(l)
        ls[ind] = str(l)

        if ind in [0,1,2,3]:
            f[ind] = f[ind].rstrip("s")
            
        if len(str(l)) == 1:
            ls[ind] = "0" + str(l)

        f[ind] = (f[ind]).replace("--", str(ls[ind]))
        ind += 1

    if ls[0] == "00":
        f[0] = ""
    if ls[1] == "00":
        f[1] = ""
    if ls[2] == "00":
        f[2] = ""    

    for s in f:
        out += str(s)

    return out

showAll = False     ## Show All Reminders
while True:
    printLine(88, "-")

    if reminders != []:
        organizedList = []
        for r in reminder_parts:
            organizedList.append(dict())        ## Create a new dictionary for every index of reminder_parts
            
        reminderIndex = 0
        for reminder in reminders:
            partIndex = -1
            for part in reminder:
                partIndex += 1
                currDict = organizedList[partIndex] ## Dictionary for the corresponding reminder_parts

                if partIndex in [2,4,5,7]:
                    p = reminder_parts[partIndex]
                    if p not in currDict.keys():
                        currDict.update({p:[]})

                    if partIndex in [2,7]:                          ## Part is 'Name of Reminder' or 'Notes'
                        (currDict[p]).append(part)
                        continue
                                    

                    elif partIndex == 4 and part.isalpha() != True:   ## Part is Date-Assigned
                        assigned = (part).split(",")
                        for i in assigned:
                            assigned[assigned.index(i)] = int(i)
                        
                        assigned = datetime(assigned[0], assigned[1], assigned[2], assigned[3], assigned[4], assigned[5])
                        (currDict[p]).append(dateTimeDiff(assigned, "now"))
                        continue
                        
                    
                    elif partIndex == 5 and part.isalpha() != True:   ## Part is Deadline
                         deadline = (part).split(",")
                         for i in deadline:
                             deadline[deadline.index(i)] = int(i)
                         
                         deadline = datetime(deadline[0], deadline[1], deadline[2], deadline[3], deadline[4], deadline[5])

                         (currDict[p]).append(dateTimeDiff("now", deadline))
                         continue

                    else:
                        raise IOError
                
                
                if part not in (currDict.keys()):   
                    currDict.update({part:[]})        ## Add new key to currDict if that key not exist

                currDict[part].append(reminderIndex)
                
            reminderIndex += 1

        now = [str(date.today().month), str(date.today().day), str(date.today().year),
             str(datetime.now().hour), str(datetime.now().minute), str(datetime.now().second)]

        print("\nToday is " + lsToStr(now, ["--/","--/","-- ~"," --:","--:","--"]))

        sortedList = []     ## List to be printed on screen
        hiddenList = []     ## Anything additional, can be shown with a future command
        dates = []          ## Due Dates in printed form


        orgInd = 0
        for d in organizedList:                 ## for {} in [{}, {}, {}]         d = {}
            if orgInd == 0:     ## Done
                for key in d.keys():                ## for key in {key:""}          key = key
                    if key != "No":
                        hiddenList += d[key]
                    else:
                        sortedList += d[key]

            elif orgInd == 1:           ## Priority
                for r in sortedList:
                    if r == "High":
                        sortedList.remove(r)
                        sortedList.insert(int(reminders[0][orgInd]),r)
                        
                    if r == "Low":
                        sortedList.remove(r)
                        sortedList.insert(int(reminders[-1][orgInd]),r)
                        
            elif orgInd == 5:   ## Due Date
                for val in d["Due Date"]:
                    if (d["Due Date"]).index(val) in sortedList:
                        dates.insert((d["Due Date"]).index(val), val)
                    
            orgInd += 1

        print("\nYou have " + str(len(sortedList)) + " unfinished reminders, and " + str(len(hiddenList)) + " hidden reminders: \n")
        
        for r in sortedList:
            Tab = " "
            lTab = len(Tab)

            l1 = str(sortedList.index(r)) + "- " + str(organizedList[2]["Name"][r])
            lenLine = len(l1)
            
            while lenLine <= 30:
                Tab += " "
                lTab = len(Tab)
                lenLine += 1
            
            print(str(sortedList.index(r) + 1) + "- " + str(organizedList[2]["Name"][r]), end=Tab)
            print("Due in " + lsToStr(organizedList[5]["Due Date"][r], ["-- years, ",
                                                                        "-- months, ", "-- days, ", "--:", "--:", "--"]), end="\t")

            deadline = (reminders[r][5]).split(",")

            print(lsToStr(deadline, ["--/", "--/", "-- (", "--:", "--", ")"]), end="\t")
            print("via " + reminders[r][6], end="\t")
            if reminders[r][7] != "":
                print("*Additional Notes")
                
        for r in hiddenList:
            if showAll != True:
                break
            else:
                print("\nHIDDEN LIST\n")
                Tab = " "
                lTab = len(Tab)

                l1 = str(hiddenList.index(r)) + "- " + str(organizedList[2]["Name"][r])
                lenLine = len(l1)
                
                while lenLine <= 30:
                    Tab += " "
                    lTab = len(Tab)
                    lenLine += 1
                
                print(str(hiddenList.index(r) + 1) + "- " + str(organizedList[2]["Name"][r]), end=Tab)
                print("Due in " + lsToStr(organizedList[5]["Due Date"][r], ["-- years, ",
                                                                            "-- months, ", "-- days, ", "--:", "--:", "--"]), end="\t")

                deadline = (reminders[r][5]).split(",")

                print(lsToStr(deadline, ["--/", "--/", "-- (", "--:", "--", ")"]), end="\t")
                print("via " + reminders[r][6], end="\t")
                if reminders[r][7] != "":
                    print("*Additional Notes")

    stillHere = True
    while stillHere:
        print()
        if reminders != []:
            cmd = input("\nREMINDERS >>> ")
        else:
            print("This reminders list is empty. You need to create a new reminder")
            cmd = "New"

        if cmd in ["New", "new", "n", "N"]:
            newReminder = []
            for part in reminder_parts:
                newReminder.append(input("\t" + str(part) + ": "))

            reminders.append(newReminder)        
            stillHere = False
            break
                

        elif cmd.lower() in ["exit", "x"]:
            if input("Are you sure you want to exit? (Y/n): ") != "n":
                exit(0)

        elif cmd.lower() in ["r", "refresh"]:
            stillHere = False
            break

        elif cmd.lower() in ["additional notes", "an"]:
            print("Type the letter and number (e.g. S1) of the corresponding reminder you want to show additional information: \n")
            for l in sortedList:
                if reminders[l][7] != "":
                    print("S" + str(sortedList.index(l) + 1) + "- " + str(reminders[l][2]))
            for l in hiddenList:
                if reminders[l][7] != "":
                    print("H" + str(hiddenList.index(l) + 1) + "- " + str(reminders[l][2]))

            into = input("\tADDITIONAL INFO >>> ")

            if "S" in into or "s" in into:
                into = into.replace("s", "")
                into = into.replace("S", "")
                print("\n" + reminders[sortedList[int(into) - 1]][7])

            elif "H" in into or "h" in into:
                into = into.replace("h", "")
                into = into.replace("H", "")
                print("\n" + reminders[hiddenList[int(into) - 1]][7])

            stillHere = False
            break

        elif cmd.lower() in ["show all", "sa"]:
            showAll = True
            stillHere = False
            break

        elif cmd.lower() in ["delete", "d"]:
            print("Type the letter and number (e.g. S1) of the corresponding reminder you want deleted: \n")
            for l in sortedList:
                print("S" + str(sortedList.index(l) + 1) + "- " + str(reminders[l][2]))
            for l in hiddenList:
                print("H" + str(hiddenList.index(l) + 1) + "- " + str(reminders[l][2]))

            into = input("\tDELETE >>> ")
            ex_into = into

            if "S" in into or "s" in into:
                into = into.replace("s", "")
                into = into.replace("S", "")
                del reminders[sortedList[int(into) - 1]]

            elif "H" in into or "h" in into:
                into = into.replace("h", "")
                into = into.replace("H", "")
                del reminders[hiddenList[int(into) - 1]]

            print("\nSuccessfully deleted reminder " + str(ex_into))
            stillHere = False
            break
                
                
        elif cmd in ["", " "]:
            continue
                
        else:
            print("Cannot determine what '" + cmd + "' means")

