# 함수를 사용한 프로그램 설계
# 1. 요구사항 철저히 분석 (명세서, 사규, 데이터 등)
# 2. 문제 분할
# 3. 함수 생성
# 4. solution을 단위테스트 및 통합테스트 완료 후, 회사에 배포, 안정화
import grade

def main():
    li = grade.readList()
    grade.sortingList(li)
    grade.showScore(li)

if __name__ == "__main__":
    main()