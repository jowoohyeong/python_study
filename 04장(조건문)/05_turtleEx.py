# 사용자에게 명령어를 입력받아 터틀그래픽 제어
# left, right 입력받기
import turtle

t = turtle.Pen()

while True:
    direction = input("left or right 입력(종료 : q): ")
    if direction == "q":
        break
    elif direction == "left":
        t.left(60)
        t.forward(50)
    elif direction == "right":
        t.right(60)
        t.forward(50)

#터틀 그래픽 창이 클릭되어야 창이 닫힘
turtle.exitonclick()