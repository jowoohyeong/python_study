# 화씨 - 섭씨온도 변환
# for 문, 실수로 화씨 0~ 100도까지 10도 단위로 증가시키면서 대응되는 섭씨 온도 출력

for f in range(0, 101, 10):
    c = (f - 32) * 5 / 9
    print(f, " -> ", round(c, 2))
