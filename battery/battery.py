from abc import ABC, abstractclassmethod

class BatteryInterface(ABC):
    
    @abstractclassmethod
    def needs_service(self):
        pass