import unittest
from tire.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensor_result= [0.0,0.3,0.5,0.9]
        tire = CarriganTire(sensor_result)
        self.assertTrue(tire.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        sensor_result= [0.0,0.3,0.5,0.8]
        tire = CarriganTire(sensor_result)
        self.assertFalse(tire.needs_service())

if __name__ == "__main__":
    unittest.main()