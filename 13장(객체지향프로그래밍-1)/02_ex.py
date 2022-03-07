from TV import Tv

if __name__ == "__main__":
    tv1 = Tv()
    tv2 = Tv()

    tv1.name = "바보상자"
    tv1.color = "검정"
    tv1.powerTV(True)
    tv1.channelUp(9)
    tv1.volumeUp(25)
    tv1.powerTV(False)
    tv1.volumeUp(26)

    tv1.__str__()