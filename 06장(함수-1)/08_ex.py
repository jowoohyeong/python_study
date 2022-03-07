# 디폴트 인수 default argument

# 매개변수 2개를 가지지만 디폴트 인수가 있어서 name에 대응되는 인수만 있어도 호출 가능
def hello(name, msg="반갑다"):
    print("안녕 "+ name+", "+ msg)
    
hello("우형")

hello("우형", "잘가라")