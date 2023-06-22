import unittest
from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
  def test_tire_should_be_serviced(self):
    sensor_result = [0,1,1,1]
    tire = OctoprimeTire(sensor_result)
    self.assertTrue(tire.needs_service())

  def test_tire_should_not_be_serviced(self):
    sensor_result = [0,0,1,1]
    tire = OctoprimeTire(sensor_result)
    self.assertFalse(tire.needs_service())

if __name__ == "__main__":
    unittest.main()