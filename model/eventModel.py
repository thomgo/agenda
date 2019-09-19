# coding: utf-8
from .connection import Connection
from .entities.event import Event

class eventModel():
    """Class to perform all queries related to the event table in the database"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        self.db = Connection()

    def get_events(self, date):
        sql = """select event_id, title, description, event_time from event
                 where event_date = %s
                 order by event_time"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date,))
        events = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(events):
            events[key] = Event(value)
        return events

    def get_single_event(self, date, hour):
        sql = """select * from event
                 where event_date = %s
                 and event_time = %s"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date, hour))
        event = self.db.cursor.fetchone()
        self.db.close_connection()
        if event:
            return Event(event)
        return False

    def add_event(self, event):
        sql = """insert into event(title, description, event_date, event_time)
                 values(%s, %s, %s, %s)"""
        arguments = (event.title, event.description, event.event_date, event.event_time)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_event(self, date, hour):
        sql = """delete from event
                 where event_date = %s
                 and event_time = %s"""
        arguments = (date, hour)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def update_event(self, event):
        sql = """update event
                 set title=%s, description=%s, event_date=%s, event_time=%s
                 where event_id=%s"""
        arguments = (event.title, event.description, event.event_date, event.event_time, event.event_id)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()
