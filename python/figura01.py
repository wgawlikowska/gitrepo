#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figura01.py
import turtle


def main(args):
    turtle.setup(800, 600)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
        turtle.done()
    turtle.pendown()
    turtle.pensize(2)
    turtle.color("red")
    
    turtle.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
