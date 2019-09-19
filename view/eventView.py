# coding: utf-8

from model.eventModel import eventModel
from model.entities.event import Event

class eventView():
    """View or controller taking care of all the logic related to event in the app."""
    model = eventModel()

    def __init__(self):
        pass

    def show_events(self):
        """Display all the events for specific date from database to the screen"""
        date = input("Vous souhaitez voir votre agenda pour quelle journée ? : ")
        events = self.model.get_events(date)
        print("\nVotre agenda du {}\n".format(date))
        if events:
            for event in events:
                print(event)
        else:
            print("Rien ce jour là, bravo vous êtes libre :-)")
        input("Tapez sur une touche pour continuer")

    def new_event(self):
        """Displays inputs to register a new event in the database"""
        event = Event()
        event.title = input('Titre : ')
        event.description = input('Description (optionnelle) : ')
        event.event_date = input('Date (jj/mm/aaaa) : ')
        event.event_time = input('Heure (hh:mm) : ')
        # Check the hour of the new event is free
        while self.model.get_single_event(event.event_date, event.event_time):
            print("Vous avez déjà quelque chose à cette heure là !")
            event.event_time = input('Nouvelle heure : ')
        self.model.add_event(event)

    def delete_event(self):
        """Display an input to delete a event from database by date and hour"""
        date = input("Jour de l'événement : ")
        hour = input("Heure de l'événement : ")
        self.model.delete_event(date, hour)

    def update_event(self):
        """Allow user to change attribut's value for specific event"""
        # Retrieve an event
        choice = ""
        while choice != "s":
            date = input("Jour de l'événement : ")
            hour = input("Heure de l'événement : ")
            event = self.model.get_single_event(date, hour)
            if event : break
            print("Nous ne trouvons rien à cette date")
            choice = input("Tapez s pour arrêter, n'importe quelle touche pour continuer")
        # If we have found an event
        if event:
            print("Voici les informations enregistrées")
            # User can change attributs as long as he wants
            while True:
                print(event)
                print("Tapez s pour arrêter")
                attribut = input("Attribut à modifier : ")
                if attribut == 's' : break
                value = input("Nouvelle valeur : ")
                # If he chooses to change the hour then we check the hour is free
                if attribut == "event_time":
                    while self.model.get_single_event(event.event_date, value):
                        print("Vous avez déjà quelque chose à cette heure là !")
                        value = input('Nouvelle heure : ')
                # Set the new value and update the database
                setattr(event, attribut, value)
            self.model.update_event(event)
