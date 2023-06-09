from Engine.engines import WilloughbyEngine

class TestWilloughby:
    def need_service_true(self):
        current_milage = 60001
        last_service_milage = 0
        engine = WilloughbyEngine(current_milage, last_service_milage)
        self.assertTrue(engine.needs_service())

    def need_service_false(self):
        current_milage = 60000
        last_service_milage = 0
        engine = WilloughbyEngine(current_milage, last_service_milage)
        self.assertFalse(engine.needs_service())
