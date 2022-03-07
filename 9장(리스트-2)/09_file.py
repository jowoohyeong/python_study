# 기본 파일 입출력
data = []
f = open("C:\\TEMP\\test.txt", mode="r", encoding="UTF-8")

print(f)
# readlines() 는 파일의 저장된 내용을 한번에 다 읽음
for line in f.readlines():
    # strip() 는 원래 양쪽 공백을 제거하지만, 파일을 읽어올땐 엔터키제거를 해준다.
    data.append(line.strip())
# 프로그램에서 리소스 사용을 마쳤으면 close() 호출해야한다.
print(data)
f.close()

# 파일에 내용 쓰기 / 모드가 w일 경우 기존 파일의 내용을 덮어쓴다.
f = open("C:\\TEMP\\test.txt", mode="w", encoding="UTF-8")
f.write("우리는 파이썬을 공부한다.")
f.write("나도 파이썬을 공부한다.")
print("쓰기완료")
f.close()

# 기존 파일에 내용 추가  /\ 모드 a
f = open("C:\\TEMP\\test.txt", mode="a", encoding="UTF-8")
f.write("aa우리는 파이썬을 공부한다.")
f.write("bb나도 파이썬을 공부한다.")
print("추가완료")
f.close()

# csv 파일 읽기
import csv
fp = open("C:\\TEMP\\test.csv", mode="r")
reader = csv.reader(fp)
for txt in reader:
    print(txt)
fp.close()