from tire.tire import TireInterface

class CarriganTire(TireInterface):
    def __init__(self, sensor_result):
        self.sensor_result = sensor_result
    
    def needs_service(self):
        for value in self.sensor_result:
            if value >= 0.9:
                return True
        return False