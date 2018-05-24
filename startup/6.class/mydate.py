class Date(object):

    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def say(self):
        print("Date[%04d-%02d-%02d]" % (self.year, self.month, self.day))

    @classmethod
    def class_gen(cls, date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        return cls(year, month, day)

    @staticmethod
    def static_gen(date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        return Date(year, month, day)


date1 = Date.class_gen('2018-03-05')
date1.say()

date2 = Date.static_gen('2018-01-03')
date2.say()
