# range() 함수 실습하기

# range() 함수 매개변수 1~3개 실습
sum1 = 0
for x in range(10):
    sum1 += x
print(sum1)
sum2 = 0
for x in range(0, 10):
    sum2 += x
print(sum2)
# range([start,] stop[, step]) 누적시킬 때 step만큼 건너띄어 리스트를 생성한다.
# 대괄호 부분은 생략가능하다.
sum3 = 0
for x in range(0, 10, 2):
    sum3 += x
print(sum3)

# 문자열 실습
word = "JO WOO HYEONG"
for ch in word:
    print(ch, end="")