import re


class SavingObjects:
    def __init__(self, date, payment, amount, product):
        self.date = date
        self.payment = payment
        self.amount = amount
        self.product = product

    def variables(self):
        return (self.date, self.payment, self.amount, self.product)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        check = re.search(r"(\d{2}|\d)/(\d{2}|\d)/(\d{4})", date)
        if check:
            self._date = date
        else:
            raise NameError("Please type the correct format dd/mm/yyyy")

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, payment):
        if type(payment) == type("Strings") and payment.lower() in [
            "cash",
            "credit",
            "others",
        ]:
            self._payment = payment

        else:
            raise TypeError("Please input a legit payment")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if type(amount) == type(11.1):
            self._amount = amount
        else:
            raise ValueError("Please type suitable amount of money: ")


def take_value(date, payment, cost, product):
    today = SavingObjects(date, payment, cost, product)
    value = today.variables()
    return value
