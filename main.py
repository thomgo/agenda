# coding: utf-8
import os
import time

from view.eventView import eventView

# Main file acting like a routing system
# Call the right method from the view, depending on user input


# Simple intro for the app
os.system('cls' if os.name == 'nt' else 'clear')
print("Bienvenue sur votre agenda personnel")
time.sleep(3)

# The action the user wants to do, by default nothing
action = ""
# while the user does not chose to leave the program
while action != 'q':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Que souhaitez vous gérez ? (c: conférences, i: intervenants, q: quitter)")
    action = input(": ")
    # call the right action function according to user input

# Leave the program
print("Merci et au revoir")
time.sleep(3)
exit()
