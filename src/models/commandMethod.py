from enum import Enum

class CommandMethod(Enum):
    GET = 'get'
    SET = 'set'
    DELETE = 'delete'
    MERGE = 'merge'
    OBSERVE = 'observe'
    SUBSCRIBE = 'subscribe'
    UNSUBSCRIBE = 'unsubscribe'
