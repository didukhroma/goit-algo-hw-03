'''
Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» 
за умови, що користувач повинен мати можливість вказати рівень рекурсії.
'''

import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(size/2, size/2)
    t.pendown()

    for _ in range(3):
        t.right(120)
        koch_curve(t, order, size)

    window.mainloop()

# Виклик функції
def main():
    recursion_level = int(input("Please enter the recursion level: "))
    draw_koch_curve(recursion_level)

if __name__ == "__main__":
    main()