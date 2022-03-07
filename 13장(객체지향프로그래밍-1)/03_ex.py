from Person import *

if __name__ =="__main__":
    # 기본 생성자 호출
    # 기본 생성자는 호출되면 무조건 똑같은 초기값을 지니고 메모리에 생성
    # 그 값을 변경하려면 직접 setter()나 인스턴스명.
    # 필드 = 값 을 대입하여 변경해야한다는 단점이 존재한다.
    p1 = Person()
    p1.__str__()
    print("--------------")
    p2 = Person()
    p2.__str__()
    print("--------------")
    print("p1.name before: ", p1.getName())
    p1.setName("김길동")
    p1.age = 50
    print("p1.name after: ", p1.getName())

    # age 라는 필드는 __ 붙지 않았기에 public 성질을 지니고 있어서 외부에서도 바로 접근이 가능하다.
    print("p1.address : ", p1.getAddress())
    print("p1.age : ", p1.age)

    # 같은 필드의 값을 가지고 있지만 서로 다른 인스턴스이다.
    print("p1의 주소 :", id(p1))
    print("p2의 주소 :", id(p2))