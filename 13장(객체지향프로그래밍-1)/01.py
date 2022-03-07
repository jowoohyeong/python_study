# 객체지향 프로그래밍 (OOP : object - oriented programming)
# 현실 세계에 있는 어떠한 사물을 코드로 표현하는 방법
# 클래스 용어 : 사물을 묘사하는 것이고 예를 들면 설계도, 붕어빵틀이다.
# 클로스 요소 : 멤버변수(필드, 속성), 멤버메서드 (기능), 생성자(필수)

class Car():
    color=""
    speed=0
    def upSpeed(self, speed):
        # self는 자바에서 this와 동일하며 자기 자신의 주소를 가지고 있는 인자이다. 인스턴스를 생성해야 self가 활성화된다.
        self.speed += speed

    def downSpeed(self, speed):
        if self.speed - speed < 0:
            print("속도는 음수일 수 없다.")
            return
        self.speed -= speed
    def printFields(self, myCar):
        print(myCar, "의 색상은", self.color, "속도는: ", self.speed)

if __name__ == "__main__":
    myCar1 = Car()
    myCar2 = Car()
    print("myCar1의 주소: ", id(myCar1))
    print("myCar2의 주소: ", id(myCar2))

    print("myCar1의 타입: ", type(myCar1))

    myCar1.color = "파랑"
    myCar1.upSpeed(10)
    myCar1.printFields("myCar1")

    myCar2.color = "노랑"
    myCar2.downSpeed(10)
    myCar2.printFields("myCar2")

# 클래스 설계 및 사용 루틴
# 1. 클래스 설계
# 2. 인스턴스 생성
# 3. 필드, 메소드 호출