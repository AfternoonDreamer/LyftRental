from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class Calliope(Car, CapuletEngine, SpindlerBattery):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engineer = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(current_date, last_service_date)
        self.this_car = Car(self.engineer, self.battery)

    def needs_service(self):
        return self.this_car.needs_service();

# class Calliope(CapuletEngine):
#     def needs_service(self):
#         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
#         if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
#             return True
#         else:
#             return False

