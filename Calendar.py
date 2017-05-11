"""In this calendar users will be able to: Add an event to the calendar, Update an existing event, Delete an existing event"""

from time import sleep, strftime 

#Get user's name
USER_FIRST_NAME = str(raw_input("What is your name? "))

#Calendar setup
calendar = {}

#Welcome
def welcome():
    print "Welcome to your calendar " + USER_FIRST_NAME + "!"
    print "Calendar is opening..."
    sleep(1)
    print "Today is " + strftime("%A %B %d, %Y")
    print "Current time is: " + strftime("%I:%M:%S")
    print "What would you like to do?"

#Calendar's functionality
def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = raw_input("Enter A to Add, U to Update, \nV to View, D to Delete, X to Exit: ").upper()

        #if V is chosen- VIEW
        if user_choice == "V":
            if len(calendar.keys()) < 1:
                print "The calendar is empty"
            else:
                print calendar

        #if U is chosen- UPDATE
        elif user_choice == "U":
            date = raw_input("What date? ")
            update = raw_input("Enter the update: ")
            update = calendar[date]
            print "Update successful."
            print calendar

        #if A is chosen -ADD
        elif user_choice == "A":
            event = raw_input("Enter event: ")
            date = raw_input("Enter date (MM/DD/YYYY): ")
            if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
                print "An invalid date was entered."
                try_again = raw_input("Try Again? Y for Yes, N for No: ").upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                calendar[date] = event

        #if D is chosen -DELETE
        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                print "The calendar is empty."
            else:
                event = raw_input("What event do you want to delete? ")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print "Event deleted successfully."
                        print calendar
                    else:
                        print "Incorrect event was entered."

        #if X is chosen -EXIT
        elif user_choice == "X":
            start = False

        #if nonsense is entered -BREAK
        else:
            print "Invalid command was entered."
            start = False

start_calendar()