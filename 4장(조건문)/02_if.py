# 조건문 if 구문만 사용!
score = 90

# 몇 십개의 if 구문이 존재하더라도, CPU는 모든 if 문을 참조한다.
# 그러므로 애플리케이션 프로그램의 성능은 떨어질 수 밖에없다.
if score >= 90: print("점수가 90점이상, A")
if score >= 80: print("점수가 80점이상, B")
if score >= 70: print("점수가 70점이상, C")
if score >= 60: print("점수가 60점이상, D")
