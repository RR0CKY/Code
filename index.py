import turtle
import colorsys

# ---------------- Screen ----------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title(" Rainbow Mandala")
screen.setup(width=1000, height=1000)
screen.tracer(0)

# ---------------- Turtle ----------------
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(1.5)


# ---------------- Petal Function ----------------
def draw_petal(size, angle, petals, hue):
    for i in range(petals):
        color = colorsys.hsv_to_rgb((hue + i / petals) % 1, 1, 1)

        t.color(color)
        t.circle(size, angle)
        t.left(360 / petals)


# ---------------- Main Mandala ----------------
layers = 8

petals_list = [
    6, 8, 10, 12, 14, 16,
    18, 20, 22, 24, 26, 28
]

size = 10
angle = 50
hue = 0.0

for i in range(layers):
    draw_petal(
        size,
        angle,
        petals_list[i],
        hue
    )

    size += 15
    hue = (hue + 0.05) % 1


# ---------------- Center Rainbow Star ----------------
t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()

t.width(2)

for i in range(12):
    color = colorsys.hsv_to_rgb(i / 12, 1, 1)
    t.color(color)

    t.forward(40)
    t.backward(40)
    t.left(30)


# ---------------- Outer Dotted Circle ----------------
t.penup()
t.goto(0, -(size + 15))
t.setheading(0)
t.pendown()

t.width(1)

for i in range(360):
    if i % 3 == 0:
        color = colorsys.hsv_to_rgb(i / 360, 1, 1)
        t.color(color)
        t.dot(5)

    t.left(1)


# ---------------- Finish ----------------
screen.update()
turtle.done()