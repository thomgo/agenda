# coding: utf-8
import psycopg2
import psycopg2.extras

class Connection():
    """Class to manage the connection, the cursor and the requests to a database"""
    # Store the username, the port and the database name as class attributs
    # In this case no host name and password because of my own configuration
    USER = "thomas"
    PORT = "5432"
    DATABASE = "agenda"

    def __init__(self):
        # The class stores an instance of pyscopg2 connection and cursor classes
        self.connection = None
        self.cursor = None

    def initialize_connection(self):
        """Instanciate a connection and a cursor and store them in the related attributs"""
        try:
            self.connection = psycopg2.connect(user = Connection.USER,
                                               port = Connection.PORT,
                                               database = Connection.DATABASE)
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)

    def close_connection(self):
        """Close both connection and cursor"""
        if(self.connection):
            self.cursor.close()
            self.connection.close()
