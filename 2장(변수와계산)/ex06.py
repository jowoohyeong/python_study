# 정수를 입력받고 시, 분, 초로 변경하는 프로그램

time = int(input("초를 입력: "))

second = time % 60
minute = (time // 60) % 60
hour = (time // 60) // 60

print(hour, "시", minute, "분", second, "초")