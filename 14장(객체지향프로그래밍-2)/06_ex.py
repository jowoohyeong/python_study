# None 참조값 : 변수가 아무 것도 가리키고 있지 않다면 None 으로 초기화를 해주는 것이 권장사항
# 모든 변수는 초기화를 해주는 것이 제일 좋다.
# None(C언어,자바에서는 null) 은 아무것도 참조하지 않고 있다는 특별한 값

class TV:
    # power = False
    # volume = 0
    # channel = 0
    def __init__(self, power, channel, volume):
        self.power = power
        self.channel = channel
        self.volume = volume

    def powerTV(self):
        self.power = not self.power

    def __str__(self):
        return "power : %s, volume: %d, 채널: %d" % (self.power, self.volume, self.channel)


if __name__ == "__main__":
    tv = None
    # 결과가 None 출력
    print(tv)
    # AttributeError TV가 생성하지 않아서  power() 호출불가
    # tv.power()
    tv = TV(True, 10, 25)
    print(tv)
    tv.powerTV()
    print("---------------------")
    print(tv)