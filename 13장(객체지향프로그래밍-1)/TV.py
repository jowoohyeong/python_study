# 클래스 tv 생성
class Tv():
    name = ""
    color = ""
    power = False
    channel = 0
    volume = 0

    def powerTV(self, power):
        # self는 자바에서 this와 동일하며 자기 자신의 주소를 가지고 있는 인자이다. 인스턴스를 생성해야 self가 활성화된다.
        self.power = power

        if self.power:
            print(self.name, " on")
        else:
            print(self.name, " off")

    def channelUp(self, channel):
        if not self.power:
            print(self.name, "가 꺼져있다.")
            return

        self.channel += channel

    def channelDown(self, channel):
        if self.channel - channel < 0:
            print("채널은 음수일 수 없다.")
            return

        if not self.power:
            print(self.name, "가 꺼져있다.")
            return
        self.channel -= channel

    def volumeUp(self, volume):
        if not self.power:
            print(self.name, "가 꺼져있다.")
            return
        self.volume += volume

    def volumeDown(self, volume):
        if not self.power:
            print(self.name, "가 꺼져있다.")
            return
        if self.volume - volume < 0:
            print("소리는 음수일 수 없다.")
            return
        self.volume -= volume
    # 현재 상태 출력
    def __str__(self):
        print("%s의 정보: %s색, 현재 채널: %d, 현재 볼륨: %d" % (self.name, self.color, self.channel, self.volume))

    # __str__()은 인스턴스의 멤버변수의 값을 찍어본느 용도로 사용된다.
    def printFields(self, myCar):
        print(myCar, "의 색상은", self.color, "속도는: ", self.speed)

