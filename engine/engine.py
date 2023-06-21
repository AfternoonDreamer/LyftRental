from abc import ABC, abstractclassmethod

class EngineInterface(ABC):
    
    @abstractclassmethod
    def needs_service(self):
        pass