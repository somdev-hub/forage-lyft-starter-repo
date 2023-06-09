from abc import ABC
from battery import Battery
from add_years import add_years

class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date,current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_date=add_years(self.last_service_date,4)
        # return self.battery_should_be_serviced
        if service_date < self.current_date:
            return True
        else:
            return False