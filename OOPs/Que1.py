class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    def debit(self, amount):
        self.balance = self.balance - amount
        print("Rs.", amount, "was debited.")
        print("Available balance:",self.get_balanca())

    def credit(self, amount):
        self.balance = self.balance + amount
        print("Rs.", amount, "was credited.")
        print("Available balance:",self.get_balanca())

    def get_balanca(self):
        return self.balance

acc1 = Account(10000, 12345)

acc1.debit(1000)
acc1.credit(2000)
