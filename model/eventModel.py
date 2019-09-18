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
        sql = """insert into event(title, description, event_date, event_time)
                 values(%s, %s, %s, %s)"""
        arguments = (event.title, event.description, event.event_date, event.event_time)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_event(self, id):
        pass

    def update_event(self, id):
        pass
