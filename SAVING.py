import re

class SavingObjects:
    def __init__(self, date, payment, amount, product):
        self._date = date
        self._payment = payment
        self._amount = amount
        self._product = product

    def variables(self):
        return [self.date, self.payment, int(self.amount), self.product]

    @property
    def check_date(self):
        return self._date
    
    @check_date.setter
    def check_date(self,date):
        check = re.search(r"(\d{2}|\d)/(\d{2}|\d)/(\d{4})", date)
        if check: 
            self._date = date
        else:
            raise NameError("Please type the correct format dd/mm/yyyy")
        
    @property
    def check_payment(self):
        return self._payment 
    
    @check_payment.setter
    def check_payment(self,payment):
        if(type(payment) == type("Strings") and payment.lower() in ["cash", "credit", "others"]):
            if(payment.lower() == "others"):
                new_pay = input("Payments: ")
                self._payment = new_pay

            self._payment = payment
        else:
            raise TypeError("Please input a legit payment")
        
    @property
    def check_amount(self):
        return self._amount
    
    @check_amount.setter
    def check_amount(self,amount):
        if(type(amount) == type(11)):
            self._amount = amount
        else:
            raise ValueError("Please type suitable amount of money: ")
    
    @classmethod
    def collect_Info(cls):
        date = input("Today is:  ")
        payment = input("Type of payment: ")
        amount = int(input("It costs: "))
        product = input("The thing is/are: ")
        return cls(date, payment, amount, product)
    
def main():
    day1 = SavingObjects.collect_Info()

main()
