from abc import ABC
from engine import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, last_service_milage, current_milage):
        self.last_service_milage = last_service_milage
        self.current_milage = current_milage

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
