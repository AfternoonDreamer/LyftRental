from abc import ABC, abstractclassmethod

class TireInterface(ABC):
    
    @abstractclassmethod
    def needs_service(self):
        pass