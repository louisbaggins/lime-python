from .envelope import Envelope
from .commandMethod import CommandMethod
from .commandStatus import CommandStatus
from .reason import Reason
from abc import ABC

class Command(Envelope):

    def __init__(self, id, from_n, to, pp, metadata,  uri, type_n, resource, method, status, reason, timeout):
        super().__init__(id, from_n, to, pp, metadata)
        self.__uri = uri
        self.__type_n = type_n
        self.__resource = resource
        self.__method = method
        self.__status = status
        self.__timeout = timeout
        self.__reason = reason

    #uri config
    @property
    def uri(self):
        return self.__uri
    
    @uri.setter
    def uri(self, value):
        if(isinstance(value, str)):
            self.__uri = value
        else:
            raise ValueError('uri must be a string')
        
    #type config
    @property
    def type_n(self):
        return self.__type_n

    @type_n.setter
    def type_n(self, value):
        if(isinstance(value, str)):
            self.__type_n = value
        else:
            raise ValueError('type_n must be a string')

    #resource config
    @property
    def resource(self):
        return self.__resource

    @resource.setter
    def resource(self, value):
        self.__resource = resource

    #method config
    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        if(isinstance(value, CommandMethod)):
            self.__method = value
        else:
            raise ValueError('value must be a CommandMethod')

    #status config
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        if(isinstance(value, CommandStatus)):
            self.__status = value
        else:
            raise ValueError('value must be a CommandStatus')

    #timeout config
    @property
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, value):
        if(isinstance(value, bool)):
            self.__timeout = value
        else:
            raise ValueError('value must be a bool')

    #reason config
    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self, value):
        if(isinstance(value, Reason)):
            self.__reason = value
        else:
            raise ValueError('value must be a Reason')


class CommandListener(ABC):
    def on_command(self, command) : pass