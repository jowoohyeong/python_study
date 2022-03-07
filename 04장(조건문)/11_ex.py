# 문자열의 중앙에 있는 문자를 추출해서 출력하는 프로그램 만들기
# 짝수일 경우 2개의 문자 출력
word = input("문자열 입력: ")
length = len(word)

if length % 2 == 0:
    print(word[length//2-1] + word[length//2])
else:
    print(word[length//2])