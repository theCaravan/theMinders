# theMinders
A CLI that lists reminders from a text file, arranges them based on importance and time.

A text file is needed so as to save and load reminders.

Sort it so as to say like this, even on two or more columns if possible:

SALAH:
    ------- XXX time left
    ------- XXX time left

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
    -----------


After the reminders are listed, this comes up:

REMINDERS:  

Like Python, this is an interface, so typing certain commands does certain things.
List of intended commands:

New                             Creates new reminder. Make sure to list what categories to add it to

Delete NAME

Done NAME                       Sets Done Category to "Yes"

notDone NAME                    Sets Done Category to "No" 

Postpone NAME to DATE at TIME   Changes Deadline Category 

Move up NAME to DATE at TIME    Changes Deadline Category

Change priority NAME to ---     Changes Priority category (i.e. "College" to "Important")

Add Note NAME = ---             Adds Additional Notes for this reminder

Exit                            exit()

Open FILE                       open(LOCATION,"r")    Opens new reminders file for reading

