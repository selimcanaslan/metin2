from error_message import error


class CostumeInfo:
    def __init__(self, full_time_price, full_time_day, day, hour, min):
        self.full_time_price = full_time_price
        self.full_time_day = full_time_day
        self.day = day
        self.hour = hour
        self.min = min

    def price_for_random_day(self):
        if self.full_time_day and self.full_time_price != 0:
            if self.day and self.hour and self.min != 0:
                full_time_costume = int(self.full_time_day) * 1440  # Kostum tam zaman (dakika)
                costume_price_per_min = int(self.full_time_price) / full_time_costume  # (dakika basina dusen fiyat)
                random_costume_min = (int(self.day) * 1440) + (int(self.hour) * 60) + int(self.min)
                random_costume_price = random_costume_min * costume_price_per_min
                return random_costume_price
