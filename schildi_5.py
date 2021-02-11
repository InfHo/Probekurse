import turtle

schildi = turtle.Turtle()

schildi.shape("turtle")

schildi.speed(30000)

schildi.width(2)

for zahl in range(1000):
    for farbe in ("MediumSpringGreen",
                  "Gold",
                  "SteelBlue",
                  "DeepPink",
                  "Aqua"):
        schildi.color(farbe)
        schildi.forward(15+zahl*3)
        schildi.right(140)
        print("zahl:",zahl)





#schildi.clear()
