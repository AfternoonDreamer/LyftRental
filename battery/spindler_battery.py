from battery.battery import BatteryInterface;

class SpindlerBattery(BatteryInterface):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.replace_frequence = 3

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.replace_frequence)
        return service_threshold_date < self.current_date
        