from datetime import datetime
from engine.capulet_engine import CapuletEngine
from car import Car
from battery.nubbin_battery import NubbinBattery

class Thovex(Car, CapuletEngine, NubbinBattery):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engineer = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        self.this_car = Car(engineer, battery)

    def needs_service(self):
        return self.this_car.needs_service();


# class Thovex(CapuletEngine):
#     def needs_service(self):
#         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
#         if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
#             return True
#         else:
#             return False
