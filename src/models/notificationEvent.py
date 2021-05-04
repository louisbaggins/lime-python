from enum import Enum

class NotificationEvent(Enum):
    FAILED = 'failed'
    ACCEPTED = 'accepted'
    VALIDATED = 'validated'
    AUTHORIZED = 'authorized'
    DISPATCHED = 'dispatched'
    RECEIVED = 'received'
    CONSUMED = 'consumed'

