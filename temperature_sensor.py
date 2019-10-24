import random
class TemperatureSensor(object):
    """"
    A class that creates a temperature object.
    """
    def check_temperature(self):
        return random.randint(-3, 38)