# 문제

class Account:
    __balance = 0

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
        print("통장에", format(amount, ","), "이 입급됨")
        print("현재 잔액 : ", format(self.getBalance(), ","), "원")

    def withdraw(self, amount):
        if self.__balance - amount < 0:
            print("통장에 돈이 부족함")
            return

        self.__balance -= amount
        print("통장에", format(amount, ","), "이 출금됨")
        print("현재 잔액 : ", format(self.getBalance(), ","), "원")

    def getBalance(self):
        return self.__balance

    def __str__(self):
        print("현재 잔액 : ", format(self.getBalance(), ","), "원")

if __name__ == "__main__":
    b = Account()
    b.deposit(1000000)
    b.withdraw(200000)
