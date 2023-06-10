from abc import ABC
from tires import Tires


class OctoprimeTire(Tires, ABC):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        if sum(self.tire_wear) >= 3.0:
            return True
        else:
            return False