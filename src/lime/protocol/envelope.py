from abc import ABC

class Envelope(ABC):

    def __init__(self, id, from_n, to, pp, metadata):
        self.__id = id
        self.__from_n = from_n
        self.__to = to
        self.__pp = pp
        self.__metadata = metadata

    @property
    def id(self):
        return self.__id

    @property
    def from_n(self):
        return self.__from_n

    @property
    def to(self):
        return self.__to
    
    @property
    def pp(self):
        return self.__pp

    @property
    def metadata(self):
        return self.__metadata