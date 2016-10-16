from abc import ABCMeta, abstractmethod

# Subject
class Payment(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def do_pay(self):
        pass


# Real Subject
class Bank(Payment):

    def __init__(self):
        self.card = None
        self.account = None


    def __get_account(self):
        self.account = self.card
        return self.account

    def __has_funds(self):
        print "Checking if account has enough funds."
        return True

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        if self.__has_funds():
            print "Bank:: Paying the merchant."
            return True
        else:
            print "Bank:: Sorry, not enough funds."
            return False

# Proxy
class DebitCard(Payment):

    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = raw_input("Enter you card number: ")
        self.bank.set_card(card)
        return self.bank.do_pay()

# Client
class User(object):

    def __init__(self):
        print "Lets buy something"
        self.debit_card = DebitCard()
        self.is_purchaged = None

    def make_payment(self):
        self.is_purchaged = self.debit_card.do_pay()

    def __del__(self):
        if self.is_purchaged:
            print "Payment was successful."
        else:
            print "Try once again"


user = User()
user.make_payment()

# Lets buy something
# Enter you card number: 1234-5678-0123-4567
# Checking if account has enough funds.
# Bank:: Paying the merchant.
# Payment was successful.
