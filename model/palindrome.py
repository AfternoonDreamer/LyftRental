from datetime import datetime
from car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery

class Palindrome(Car, SternmanEngine, SpindlerBattery):
    def __init__(self, current_date, last_service_date, warning_light_on):
        engineer = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        self.this_car = Car(engineer, battery)

    def needs_service(self):
        return self.this_car.needs_service();


# class Palindrome(Car, SternmanEngine, SpindlerBattery):
#     def __init__(self, current_date, last_service_date, warning_light_on):
#         engineer = super(SternmanEngine, self).__init__(warning_light_on)
#         battery = super(SpindlerBattery, self).__init__(current_date, last_service_date)
#         self.this_car = super(Car, self).__init__(engineer, battery)

#     def needs_service(self):
#         return self.this_car.needs_service();



# class Palindrome(SternmanEngine):
#     def needs_service(self):
#         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
#         if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
#             return True
#         else:
#             return False
