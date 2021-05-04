from .reason import Reason
from .notificationEvent import NotificationEvent
from envelope import Envelope
from abc import ABC, abstractmethod

class Notification(Envelope):

    @property
    @abstractmethod
    def event(self):
        return self.__event

    @event.setter
    @abstractmethod
    def event(self, value):
        if(isinstance(value, NotificationEvent)):
            self.__event = value
        else:
            raise ValueError('value must be a ''NotificationEvent''')

class NotificationListener(ABC):
    def on_notification(self, notification) : pass