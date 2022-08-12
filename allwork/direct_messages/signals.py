from django.dispatch import Signal


#providing_args = ['from_user', 'to']

message_sent = Signal()
#message_sent.receivers = providing_args

message_read = Signal()
#message_read.receivers = providing_args
