# 두 set의 사람중 중복된 사람을 출력

A = {"조우형", "김연아", "손연재", "김철수"}
B = set("최앙락 김기훈 손연재 안철수".split())
print("2개의 파티에 모두 참석한 사람은 아래와 같다.")
print(A & B)
print(A.intersection(B))