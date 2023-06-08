from abc import ABC
from battery import Battery

class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date,current_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.current_date = current_date

    def battery_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000

    def needs_service(self):
        return self.battery_should_be_serviced