#

# TODO consider false/true ?
OFF = 0
ON = 1

class MyFakeBulb:
    def __init__(self, bulb_name):
        self.label = bulb_name
        self.power = OFF
        self.brightness = 0
        self.bulb = {}  # FIXME

def set_power(iterator_of_bulbs, new_state=True):
    # iterator_of_bulbs - probably a list
    for bulb in iterator_of_bulbs:
        print('set_power %r' % ((bulb, new_state),))

"""
set_power ({}, True)
send '[{"success": {"/lights/1/state/on": true}}]'

set_power ({}, False)
send '[{"success": {"/lights/1/state/on": false}}]'

"""

def get_state(bulbs):
    return bulbs

def find_bulbs(timeout=1):
    #return []
    return [
        MyFakeBulb('fake bulb 1')
    ]

