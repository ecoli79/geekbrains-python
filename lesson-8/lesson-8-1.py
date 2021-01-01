# lesson-8 example 1
# working with class advanced methods

class Date:
    def __init__(self, in_date):
        self.date = in_date

    @classmethod
    def extract_date(cls, in_date):
        date = []
        try:
            for d in in_date.split("-"):
                date.append(int(d))
            return cls(date)

        except ValueError:
            return cls([int("01"), int("01"), int("1900")])

    @staticmethod
    def checking_date(obj):
        if obj.date[0] not in range(1, 32):
            print("День не может быть меньше 1 или больше 31")

        if obj.date[1] not in range(1, 13):
            print("Месяц не может быть меньше 1 или больше 12")

        if obj.date[2] not in range(1900, 3001):
            print("Год не может быть меньше 999 или больше 3001")


new_date = Date.extract_date("11-11-3002")

print(new_date.date)
Date.checking_date(new_date)
