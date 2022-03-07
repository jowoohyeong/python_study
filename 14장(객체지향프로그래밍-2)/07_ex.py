# 클래스 안의 상수를 많이 사용함.
# 상수는 보통 클래스변수 형태로 지정하여 사용
class Character:
    # 상수값 정의
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERY_STRONG = 30

    def __init__(self):
        self.__hp = Character.NORMAL

    def levelUp(self):
        self.__hp = Character.STRONG

    def damage(self):
        self.__hp = Characterg.WEAK

    def getHp(self):
        return self.__hp

    # __str__()은 문자열을 리턴하게끔 해주는것 이 주목적이다.
    def __str__(self):
        return "HP : " + str(self.__hp)

if __name__ == "__main__":
    ch = Character()
    print(ch)
    ch.levelUp()
    print(ch)
    ch.damage()
    print(ch)