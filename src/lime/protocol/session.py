from envelope import Envelope
from .reason import Reason
from enum import Enum
from abc import ABC, abstractmethod

class SessionState(Enum):
    NEW = 'new'
    NEGOTIATING = 'negotiating'
    AUTHENTICATING = 'authenticating'
    ESTABLISHED = 'established'
    FINISHING = 'finishing'
    FINISHED = 'finished'
    FAILED = 'failed'

class SessionEncryption(Enum):
    NONE = 'none'
    TLS = 'tls'

class SessionCompression(Enum):
    NONE = 'none'
    GZIP = 'gzip'

class Session(Envelope):

    @property
    @abstractmethod
    def state(self):
        return self.__state

    @state.setter
    @abstractmethod
    def state(self, value):
        if(isinstance(value, SessionState)):
            self.__state = value
        else:
            raise ValueError('state must be a SessionState')

    @property
    @abstractmethod
    def encryption(self):
        return self.__encryption

    @encryption.setter
    @abstractmethod
    def encryption(self, value):
        if(isinstance(value, SessionEncryption())):
            self.__encryption = value
        else:
            raise ValueError('encryption must be a SessionEncryption')

    @property
    @abstractmethod
    def encryption_options(self):
        return self.__encryption_options

    @encryption_options.setter
    @abstractmethod
    def encryption_options(self, value):
        if(isinstance(value, list) and all(isinstance(v, SessionEncryption) for v in value)):
            self.__encryption = value
        else:
            raise ValueError('Encryption must be a SessionEncryption')

    
    @property
    @abstractmethod
    def compression(self):
        return self.__compression

    @compression.setter
    @abstracmethod
    def compression(self, value):
        if(isinstance(SessionCompression)):
            self.__compression = value
        else:
            raise ValueError('compression must be a SessionCompression')