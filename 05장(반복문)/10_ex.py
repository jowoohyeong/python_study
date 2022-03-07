# 터틀 그래픽을 활용하여 별 모양

import turtle

t = turtle.Pen()

for i in range(5):
    t.forward(100)
    t.right(144)

# 터틀 그래픽 창이 클릭되어야 창이 닫힘
turtle.exitonclick()