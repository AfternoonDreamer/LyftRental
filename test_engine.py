import unittest
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30001
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
      
    def test_engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
  
class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 60001
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
      
    def test_engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 60000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())
      
    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


if __name__ == "__main__":
  unittest.main()