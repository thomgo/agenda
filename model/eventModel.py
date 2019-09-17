# coding: utf-8
from .connection import Connection
from .entities.event import Event

class eventModel():
    """Class to perform all queries related to the event table in the database"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        self.db = Connection()

    def get_events(self):
        pass

    def add_event(self, event):
        pass

    def delete_event(self, id):
        pass

    def update_event(self, id):
        pass
