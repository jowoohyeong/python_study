# 터틀 그래픽을 활용하여 별 모양

import turtle

t = turtle.Pen()

for i in range(6):
    t.left(20)
    for j in range(4):
        t.forward(100)
        t.right(90)

# 터틀 그래픽 창이 클릭되어야 창이 닫힘
turtle.exitonclick()