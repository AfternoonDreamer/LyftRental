from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from datetime import date
from model.calliope import Calliope
from model.palindrome import Palindrome
from model.glissade import Glissade
from model.rorschach import Rorschach
from model.thovex import Thovex


# test engine
print(CapuletEngine(60000,20000).needs_service()) # True
print(CapuletEngine(60000,40000).needs_service()) # False
print(WilloughbyEngine(160000,20000).needs_service()) # T
print(WilloughbyEngine(60000,20000).needs_service()) # F
print(SternmanEngine(False).needs_service()) # F

# test battery
print("battery: ")
print(NubbinBattery(date(2023,1,1),date(2020,1,1)).needs_service()) # F
print(SpindlerBattery(date(2022,1,1),date(2020,1,1)).needs_service()) # F


# test model
print("model: ")
print(Palindrome(date(2023,1,1), date(2020,1,1), False).needs_service())
print(Calliope(date(2023,1,1), date(2020,1,1), 60000, 20000).needs_service())
print(Glissade(date(2023,1,1), date(2020,1,1), 60000, 20000).needs_service())
print(Rorschach(date(2023,1,1), date(2020,1,1), 60000, 20000).needs_service())
print(Thovex(date(2023,1,1), date(2020,1,1), 60000, 20000).needs_service())


