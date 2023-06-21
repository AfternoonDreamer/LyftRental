from abc import ABC, abstractclassmethod

class ServiceInterface(ABC):
    
    @abstractclassmethod
    def needs_service(self):
        pass