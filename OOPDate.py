class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, day2):
        if not isinstance(day2, Date):
            return 'Вторая переменная должна быть типа Date'
        days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        date_1_from_beginning = sum(days_in_month[:(self.month - 1)]) + self.day
        date_2_from_beginning = sum(days_in_month[:(day2.month - 1)]) + day2.day
        result = date_1_from_beginning - date_2_from_beginning
        return result


jan5 = Date(1, 5)
jan1 = Date(1, 1)
print(jan5 - jan1)
print(jan1 - jan5)
print(jan1 - jan1)
print(jan5 - jan5)

mar5 = Date(3, 1)
jan1 = Date(1, 1)
print(mar5 - jan1)
print(jan1 - mar5)
print(jan1 - jan1)
print(mar5 - mar5)
