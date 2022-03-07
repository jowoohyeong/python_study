# csv 파일 읽기

# read() : 파일을 처음부터 끝까지 읽을 때 사용
# readline() : 파일의 내용을 한 줄씩 읽어들일때 사용
# readlines() : 파일을 읽으면 한 줄, 한 줄이 각각 리스트의 원소로 들어감
def main():
    c = open("sample.csv", mode="r")
    for line in c.readlines():
        # 공백 문자 제거하기
        line = line.strip()
        print(line)

        # 한 라인을 단어로 분리한다.
        words = line.split(",")
    c.close()

if __name__ == "__main__":
    main()