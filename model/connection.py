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

    def make_request(self, sql, arguments=False, message=False):
        """General method to handle a sql request with arguments and an error message"""
        try:
            self.initialize_connection()
            # execute the given sql query with arguments if there are
            self.cursor.execute(sql, arguments)
            # if the request is of type select we return a fetch with all results
            if sql.lower().startswith("select", 0):
                return self.cursor.fetchall()
            # if it is not a select then we have to commit whatever happens
            self.connection.commit()
            # if the request is of type delete we have to know if something has been deleted
            if sql.lower().startswith("delete", 0):
                # if nothing has been deleted
                if self.cursor.rowcount == 0:
                    raise Exception("Nothing found")
                return self.cursor.rowcount
            # if the request was of type insert into and was a success then return True
            return True
        except Exception as e:
            # If a specefic message has been given print it otherwise print the exception
            if message:
                print(message)
            else:
                print(e)
            return False
        finally:
            self.close_connection()
