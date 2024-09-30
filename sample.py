from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("Light bulb is on")

    def turn_off(self):
        print("Light bulb is off")


class Fan(Switchable):
    def turn_on(self):
        print("Fan is on")

    def turn_off(self):
        print("Fan is off")


class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        self.device.turn_on()
        # Logic to turn off the device later can be added here
