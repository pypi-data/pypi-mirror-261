from datetime import date, datetime, timedelta


class EDate(date):
    def datetime(self):
        return datetime(self.year, self.month, self.day)

    def tomorrow(self):
        return (self.datetime() + timedelta(days=1)).date()

    def yesterday(self):
        return (self.datetime() - timedelta(days=1)).date()

    def first_day_of_month(self):
        return self.replace(day=1)

    def first_day_of_year(self):
        return self.replace(day=1, month=1)

    def last_day_of_month(self):
        dt = self.datetime()
        while dt.day != 1:
            dt += timedelta(days=1)

        return (dt - timedelta(days=1)).date()

    def last_day_of_year(self):
        return self.replace(day=31, month=12)

    def first_day_of_last_month(self):
        return self.replace(day=1).yesterday().replace(day=1)

    def first_day_of_last_year(self):
        return super().replace(day=1, month=1, year=self.year-1)

    def last_day_of_last_month(self):
        return self.replace(day=1).yesterday()

    def last_day_of_last_year(self):
        return super().replace(day=31, month=12, year=self.year-1)
