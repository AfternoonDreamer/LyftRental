from tire.tire import TireInterface

class OctoprimeTire(TireInterface):
    def __init__(self, sensor_result):
        self.sensor_result = sensor_result

    def needs_service(self):
        sum = 0
        for value in self.sensor_result:
            sum += value
        return sum >= 3