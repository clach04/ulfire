#

# TODO consider false/true ?
OFF = 0
ON = 1

class MyFakeBulb:
    def __init__(self, bulb_name):
        self.label = bulb_name
        self.power = OFF
        self.brightness = 0

def get_state(bulbs):
    return bulbs

def find_bulbs(timeout=1):
    #return []
    return [
        MyFakeBulb('fake bulb 1')
    ]

