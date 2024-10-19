from Loto import *
import random


width = 600
height = 600

canvas_width = width-25
canvas_height = height-25


result = {
    "value1":None,
    "value2":None,
    "value3":None,
}

place1 = {
    "x1": canvas_width+(25-canvas_width)*(3/3)+10,
    "y1": canvas_height/2+100-10,
    "x2": canvas_width+(25-canvas_width)*(2/3)-10,
    "y2": canvas_height/2-100+10
}

place2 = {
    "x1": canvas_width+(25-canvas_width)*(1/3)-10,
    "y1": canvas_height/2+100-10,
    "x2": canvas_width+(25-canvas_width)*(2/3)+10,
    "y2": canvas_height/2-100+10
}

place3 = {
    "x1": canvas_width-25-10,
    "y1": canvas_height/2+100-10,
    "x2": canvas_width+(25-canvas_width)*(1/3)+10,
    "y2": canvas_height/2-100+10
}

color = {
    1: "red",
    2: "orange",
    3: "yellow"
}

