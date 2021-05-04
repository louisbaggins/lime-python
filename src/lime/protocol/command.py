from .envelope import Envelope
from .commandMethod import CommandMethod
from .commandStatus import CommandStatus
from .reason import Reason
from abc import ABC

class Command(Envelope):

    #uri config
    @property
    @abstractmethod
    def uri(self):
        return self.__uri
    
    @uri.setter
    @abstractmethod
    def uri(self, value):
        if(isinstance(value, str)):
            self.__uri = value
        else:
            raise ValueError('uri must be a string')
        
    #type config
    @property
    @abstractmethod
    def type_n(self):
        return self.__type_n

    @type_n.setter
    @abstractmethod
    def type_n(self, value):
        if(isinstance(value, str)):
            self.__type_n = value
        else:
            raise ValueError('type_n must be a string')

    #resource config
    @property
    @abstractmethod
    def resource(self):
        return self.__resource

    @resource.setter
    @abstractmethod
    def resource(self, value):
        self.__resource = resource

    #method config
    @property
    @abstractmethod
    def method(self):
        return self.__method

    @method.setter
    @abstractmethod
    def method(self, value):
        if(isinstance(value, CommandMethod)):
            self.__method = value
        else:
            raise ValueError('value must be a CommandMethod')

    #status config
    @property
    @abstractmethod
    def status(self):
        return self.__status
    
    @status.setter
    @abstractmethod
    def status(self, value):
        if(isinstance(value, CommandStatus)):
            self.__status = value
        else:
            raise ValueError('value must be a CommandStatus')

    #timeout config
    @property
    @abstractmethod
    def timeout(self):
        return self.__timeout

    @timeout.setter
    @abstractmethod
    def timeout(self, value):
        if(isinstance(value, bool)):
            self.__timeout = value
        else:
            raise ValueError('value must be a bool')

    #reason config
    @property
    @abstractmethod
    def reason(self):
        return self.__reason

    @reason.setter
    @abstractmethod
    def reason(self, value):
        if(isinstance(value, Reason)):
            self.__reason = value
        else:
            raise ValueError('value must be a Reason')


class CommandListener(ABC):
    def on_command(self, command) : pass