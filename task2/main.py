import turtle
import sys


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        new_size = size / 3
        new_order = order - 1

        koch_curve(t, new_order, new_size)
        t.left(60)
        koch_curve(t, new_order, new_size)
        t.right(120)
        koch_curve(t, new_order, new_size)
        t.left(60)
        koch_curve(t, new_order, new_size)


def draw_koch_snowflake(order, size=400):
    window = turtle.Screen()
    window.setup(width=800, height=800)
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pensize(2)

    t.penup()
    t.goto(-size / 2, size / 2 / 1.732)
    t.pendown()

    print(f"Drawing Koch Snowflake of order {order}...")
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    print("Welcome to the Koch Curve programm!")
    try:
        order = int(
            input("Please enter the recursion level (order) for the Koch Snowflake: ")
        )

        draw_koch_snowflake(order)

    except ValueError:
        print("Invalid input. Please enter a whole number for the recursion level.")
        sys.exit(1)
