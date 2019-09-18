# coding: utf-8

from model.eventModel import eventModel
from model.entities.event import Event

class eventView():
    """View or controller taking care of all the logic related to event in the app."""
    model = eventModel()

    def __init__(self):
        pass

    def show_events(self, date):
        """Display all the events from database to the screen"""
        events = self.model.get_events(date)
        print("\nVotre agenda du {}\n".format(date))
        if events:
            for event in events:
                print(event)
        else:
            print("Rien ce jour là, bravo vous êtes libre :-)")
        input("Taper sur une touche pour continuer")

    def new_event(self):
        """Displays inputs to register a new event in the database"""
        event = Event()
        event.title = input('Titre : ')
        event.description = input('Description (optionnelle) : ')
        event.event_date = input('Date (jj/mm/aaaa) : ')
        event.event_time = input('Heure (hh:mm) : ')
        self.model.add_event(event)

    def delete_event(self):
        """Display an input to delete a event from database by his ID"""
        date = input("Jour de l'événement : ")
        hour = input("Heure de l'événement : ")
        self.model.delete_event(date, hour)
