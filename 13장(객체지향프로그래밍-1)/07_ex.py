# 인스턴스 변수: 인스턴스를 생성해야 비로소 사용할 수 있는 변수
# 인스턴스 변수는메모리 공간에 독립적으로 공간을 차지하고 있어서 해당 인스턴스에게만 영향을 끼친다.
# 인스턴스 변수 접근 방법 : 인스턴스명.잇느턴스 변수명
# 클래스 변수 : 클래스가 로딩되면서 메모리 상당(메소드 영역, 클래스 영역) 미리 공간을 할당하고 저장함.
# 클래스 변수는 모든 인스턴스에게 공유되는 변수이다.
# 클래스 변수 접근 방법 : 클래스명.클래스 변수명(권장)
# 클래스 변수의 값 변경은 모든 인스턴스에 영향을 끼침
# 클래스 변수는 인스턴스 생성없이도 접근 가능
class Car:
    # Car클래스의 필드
    color = ""
    speed = 0
    count = 0

    def __init__(self):
        self.color = "노랑"
        self.speed = 0
        Car.count += 1

    def __str__(self):
        print("color : ", self.color, ", speed : ", self.speed)
        # 아래는 클래스 변수에 접근하는 방법 2가지이다.
        # 객체지향 개념에서는 클래스명.클래스변수명으로 접근하는 것이 올바른 방법
        print("Car.count : ", Car.count)
        # print("count : ", self.count)


if __name__ == "__main__":
    print(Car.count)   # 인스턴스를 생성않아도 값이 출력.
    print(id(Car.count))
    # 인스턴스 생성
    car1 = Car()
    car1.__str__()
    # 파이썬에서는 인스턴스를 생성하면 메모리의 값이 새로이 할당됨을 알수가 있다.
    print(id(car1.count))
    print(id(Car.count))
    car2 = Car()
    car2.__str__()
    print(id(car2.count))
    print(id(Car.count))