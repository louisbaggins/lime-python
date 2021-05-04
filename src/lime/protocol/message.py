from abc import ABC, abstractmethod
from envelope import Envelope
class Message(Envelope):

    #type config
    @property
    @abstractmethod
    def type(self): 
        return self.__type_n
    
    @type.setter
    @abstractmethod
    def type(self, value):
        if(isinstance(value, str)):
            self.__type_n
        else:
            raise ValueError('value must be a string')

    #content config
    @property()
    @abstractmethod
    def content(self):
        return self.__content

    @content.setter
    @abstractmethod
    def content(self, value):
        self.__content = value

class MessageListener(ABC):
    def on_message(self, message) : pass