import turtle

from argparse import ArgumentParser


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size / 2)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def main(order=3, size=1000):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 3, size / 4)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-o", "--order", default="3", help="Koch curve's order (defaults to 3)"
    )
    args = parser.parse_args()
    main(int(args.order))
