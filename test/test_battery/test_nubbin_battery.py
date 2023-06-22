import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date(2023, 6, 21) 
        last_service_date = date(2018, 6, 21) 
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date(2023, 6, 21) 
        last_service_date = date(2020, 6, 21) 
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    
if __name__ == "__main__":
  unittest.main()