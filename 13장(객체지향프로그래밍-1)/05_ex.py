# 문제
from math import *
class Circle:
    __radius = 0

    def __init__(self, radius):
        self.__radius = radius

    def calcArea(self):
        return pi * self.__radius ** 2

    def calcCircum(self):
        return 2 * pi * self.__radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def __str__(self):
        print("원의 반지름 :", self.getRadius())
        print("원의 넓이 : %.2f" % self.calcArea())
        print("원의 둘레 : %.2f" % self.calcCircum())


if __name__ == "__main__":
    # 매개변수가 있는 생성자를 호출하는 방법
    monitor1 = Circle(10)
    monitor1.__str__()