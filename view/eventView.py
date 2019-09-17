# coding: utf-8

from model.eventModel import eventModel
from model.entities.event import Event

class eventView():
    """View or controller taking care of all the logic related to event in the app."""
    model = eventModel()

    def __init__(self):
        pass

    def show_events(self):
        """Display all the events from database to the screen"""
        pass

    def new_event(self):
        """Displays inputs to register a new event in the database"""
        pass

    def delete_event(self):
        """Display an input to delete a event from database by his ID"""
        pass
