# coding: utf-8
from .connection import Connection
from .entities.event import Event

class eventModel():
    """Class to perform all queries related to the event table in the database"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        self.db = Connection()

    def get_events(self, date):
        """Select all events on a specific date from the database"""
        sql = """select event_id, title, description, event_time from event
                 where event_date = %s
                 order by event_time"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date,))
        events = self.db.cursor.fetchall()
        self.db.close_connection()
        # Turn each list from events into an event object
        for key, value in enumerate(events):
            events[key] = Event(value)
        return events

    def get_single_event(self, date, hour):
        """Get on event by date and hour from database"""
        sql = """select * from event
                 where event_date = %s
                 and event_time = %s"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date, hour))
        # we want a single event so we use fetch one
        event = self.db.cursor.fetchone()
        self.db.close_connection()
        # This function is used for checking
        # So if we find something we return an event object, otherwise false
        if event:
            return Event(event)
        return False

    def add_event(self, event):
        """Insert an event object into the database"""
        sql = """insert into event(title, description, event_date, event_time)
                 values(%s, %s, %s, %s)"""
        arguments = (event.title, event.description, event.event_date, event.event_time)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_event(self, date, hour):
        """Delete an event from databse with date and hour"""
        sql = """delete from event
                 where event_date = %s
                 and event_time = %s"""
        arguments = (date, hour)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def update_event(self, event):
        """Update and event object in the database"""
        sql = """update event
                 set title=%s, description=%s, event_date=%s, event_time=%s
                 where event_id=%s"""
        arguments = (event.title, event.description, event.event_date, event.event_time, event.event_id)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()
