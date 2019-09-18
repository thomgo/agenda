class Event():
    """Class representing the event entity"""

    def __init__(self, data=False):
        self.event_id = None
        self.title = None
        self.description = None
        self.event_date = None
        self.event_time = None
        if data:
            self.hydrate(data)

    def hydrate(self, data):
        """Set object's attributs value if they exists from a dictionnary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return """~~~~~~~~~~~~~~~~~~~~~~~~
{} : {}
{}""".format(self.event_time, self.title, self.description)
