class NotificationModel:
    """A notification model for notifs which will be sent to an IOT device.
    message: a string message
    ttl: time to live, a duration in seconds of how long notif is displayed
    creation_date: timestamp added during creation of notif
    notif_category: category description such as Information or Warning
    id: a counter recording the number of times a specific notif has been displayed
    displayed_times: a boolean value that shows whether a notif has been displayed at least once    
    """

    """def __init__(self, message: str, ttl: int, notification_category: str):
        self.id = 0     # automatically increment counter for each API call to Notification instance
        self.message = message
        self.ttl = ttl
       # self.creation_date = creation_date
        self.notification_category = notification_category
        self.displayed_times = 0"""
        

    def __init__(self, message, ttl, notification_category):
        self.id = 0
        self.message = message
        self.ttl = ttl
        self.notification_category = notification_category
        self.displayed_times = 0