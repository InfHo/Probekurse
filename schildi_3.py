import turtle

schildi = turtle.Turtle()

schildi.shape("turtle")

schildi.speed(3000)

schildi.width(2)

for zahl in range(1000):
    schildi.color("MediumSpringGreen")
    schildi.forward(15+zahl)
    schildi.right(70)
    print("zahl:",zahl)





#schildi.clear()
