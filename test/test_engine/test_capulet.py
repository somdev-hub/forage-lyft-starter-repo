import unittest
from Engine.engines.CapuletEngine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def need_service_true(self):
        current_milage = 30001
        last_service_milage = 0
        engine = CapuletEngine(current_milage, last_service_milage)
        self.assertTrue(engine.needs_service())

    def need_service_false(self):
        current_milage = 30000
        last_service_milage = 0
        engine = CapuletEngine(current_milage, last_service_milage)
        self.assertFalse(engine.needs_service())
