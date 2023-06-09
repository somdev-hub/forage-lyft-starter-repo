import datetime
from Battery.batteries import NubbinBattery
import unittest

class TestNubbin(unittest.TestCase):
    def need_service_true(self):
        current_date = datetime.date(2020, 1, 1)
        last_service_date = datetime.date(2016, 1, 1)
        battery = NubbinBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())
    def need_service_false(self):
        current_date = datetime.date(2020, 1, 1)
        last_service_date = datetime.date(2019, 1, 1)
        battery = NubbinBattery(last_service_date,current_date)
        self.assertFalse(battery.needs_service())