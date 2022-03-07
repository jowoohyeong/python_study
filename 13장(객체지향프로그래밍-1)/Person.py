# 생성자에 대한 실습
# 개념 : 인스턴스를 생성하기 위해서 꼭 피료한 존재이다.
# 필드의 초기화 메서드 역할
# __init__() 작성해줌으로써 생성자가 호출
# 만약 클래스에 생성자가 존재하지 않으면 인터프리터가 알아서 하나의 기본생성자를 추가
class Person:
    # __를 붙이면 private 성질으로 클래스 내부에서만 접근 가능
    # 외부에서는 접근 불가
    __name = ""
    # __가 붙지 아니하면 public 성질
    # 클래스 내부이건 외부이건 다 접근이 가능하다.
    age = 0
    height = 0
    weight = 0
    address = ""

    def __init__(self):
        self.__name = "조우형"
        self.age = 23
        self.height = 165
        self.weight = 70
        self.address = "서울"
        print("기본생성자 호출")

    # 리턴 값만 존재하고 매개변수는 존재X
    def getName(self):
        return self.__name

    def getAge(self):
        return self.age

    def getHeight(self):
        return self.height

    def getWeight(self):
        return self.weight

    def getAddress(self):
        return self.address

    def setName(self, name):
        self.__name = name

    # __str()__ 멤버변수의 값을 간단하게 확인하고자 할 때 사용하면 편리,
    #  자바언어의 toString()와 유사.
    def __str__(self):
        print(self.__name)
        print(self.age)
        print(self.height)
        print(self.weight)
        print(self.address)