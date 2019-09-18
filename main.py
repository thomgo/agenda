# coding: utf-8
import os
import time
import calendar
import locale
from datetime import datetime

from view.eventView import eventView

# Main file acting like a routing system
# Call the right method from the view, depending on user input

# Simple intro for the app
os.system('cls' if os.name == 'nt' else 'clear')
print("Bienvenue sur votre agenda personnel")
time.sleep(3)

# Set locale zone to France and get the current month and year to display right calendar
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
currentYear = datetime.now().year
currentMonth = datetime.now().month

# The action the user wants to do, by default nothing
action = ""
# while the user does not chose to leave the program
while action != 'q':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Nous sommes le : {}".format(datetime.today().strftime('%d %B %Y')))
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print (calendar.month(currentYear, currentMonth, 2, 1))
    print("Que souhaitez vous gérer ? (s: suivant, p: précédent, q: quitter)")
    action = input(": ")
    # call the right action function according to user input
    if action == "s":
        if currentMonth < 12:
            currentMonth += 1
        else:
            currentMonth = 1
            currentYear += 1
    elif action == "p":
        if currentMonth > 1:
            currentMonth -= 1
        else:
            currentMonth = 12
            currentYear -= 1

# Leave the program
print("Merci et au revoir")
time.sleep(3)
exit()
