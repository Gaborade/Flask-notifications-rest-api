from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from datetime import datetime
from pytz import utc
from .models import NotificationModel
from .http_status import HttpStatus



class NotificationManager():
    """Persisting notification model instances using an in-memory dictionary"""
    last_id = 0

    def __init__(self):
        self.notifications = {}

    
    def insert_notification(self, notification):
        """Receives a recently created NotificationModel instance as an argument and stores in dictionary"""
        # class attributes/variables can be accessed in regular instance methods using __class__ syntax
        self.__class__.last_id += 1
        # assign notif id to class variable increment
        notification.id = self.__class__.last_id
        # store notification in dictionary 
        self.notifications[self.__class__.last_id] = notification


    def get_notification(self, id):
        """Returns a NotificationModel instance through id as an argument"""
        return self.notifications[id]

    
    def delete_notification(self, id):
        """"Deletes a NotificationModel instance through id as an argument"""
        del self.notifications[id]





    