# 문자열 리스트 함축
list = "KOREA 대한민국 서울특별시 한라산 END".split()
# 첫 글자
first = [word[0] for word in list]
print(first)
# 마지막 글자
last = [word[-1] for word in list]
print(last)
# 길이
lens = [len(word) for word in list]
print(lens)

# 상호곱 Cross product
colors = "while silver black".split()
cars = "bmw5 sonata malibu sm6".split()

colored_cars = [x+"-"+y for x in colors for y in cars]
print(colored_cars)