from Car import Car
from Engine.engines.CapuletEngine import CapuletEngine
from Engine.engines.SternmanEngine import SternmanEngine
from Engine.engines.WilloughbyEngine import WilloughbyEngine
from Battery.batteries.NubbinBattery import NubbinBattery
from Battery.batteries.SpindlerBattery import SpindlerBattery


class CarFactory():
    def create_calliope(current_date, last_service_date, current_milage, last_service_milage):
        engine = CapuletEngine(last_service_milage, current_milage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_glissade(current_date, last_service_date, current_milage, last_service_milage):
        engine = WilloughbyEngine(last_service_milage, current_milage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_rorschach(current_date, last_service_date, current_milage, last_service_milage):
        engine = WilloughbyEngine(last_service_milage, current_milage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_thovex(current_date, last_service_date, current_milage, last_service_milage):
        engine = CapuletEngine(last_service_milage, current_milage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
