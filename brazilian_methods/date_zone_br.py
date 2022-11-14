from datetime import datetime, timedelta

class DateRegistration:
    def __init__(self):
        self.date_registration = datetime.today()

    def __str__(self):
        return self.date_format()

    def month_registration(self):
        months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
        return months[self.date_registration.month - 1]

    def weekday_registration(self):
        weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
        return weekdays[self.date_registration.weekday()]

    def date_format(self):
        return self.date_registration.strftime('%Y/%m/%d, %H h %M min')

    def time_registration(self):
        return datetime.today() - self.date_registration