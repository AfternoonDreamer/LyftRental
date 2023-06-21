# from abc import ABC, abstractmethod
from serviceable import ServiceInterface

class Car(ServiceInterface):
    def __init__(self, engineer, battery):
        self.engineer = engineer
        self.battery = battery

    def needs_service(self):
        return self.engineer.needs_service() or self.battery.needs_service()
