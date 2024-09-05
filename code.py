import turtle
import string
import re

SCREEN_WIDTH = 400  
SCREEN_HEIGHT = 400
MARGIN = 20 

def draw_rose(color, scale=1.0):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(10 * scale, 180)
    turtle.circle(25 * scale, 110)
    turtle.left(50)
    turtle.circle(60 * scale, 45)
    turtle.circle(20 * scale, 170)
    turtle.right(24)
    turtle.fd(30 * scale)
    turtle.left(10)
    turtle.circle(30 * scale, 110)
    turtle.fd(20 * scale)
    turtle.left(40)
    turtle.circle(90 * scale, 70)
    turtle.circle(30 * scale, 150)
    turtle.right(30)
    turtle.fd(15 * scale)
    turtle.circle(80 * scale, 90)
    turtle.left(15)
    turtle.fd(45 * scale)
    turtle.right(165)
    turtle.fd(20 * scale)
    turtle.left(155)
    turtle.circle(150 * scale, 80)
    turtle.left(50)
    turtle.circle(150 * scale, 90)
    turtle.end_fill()
    
    # Petal 1
    turtle.left(150)
    turtle.circle(-90 * scale, 70)
    turtle.left(20)
    turtle.circle(75 * scale, 105)
    turtle.setheading(60)
    turtle.circle(80 * scale, 98)
    turtle.circle(-90 * scale, 40)
    
    # Petal 2
    turtle.left(180)
    turtle.circle(90 * scale, 40)
    turtle.circle(-80 * scale, 98)
    turtle.setheading(-83)
    
    # Leaves 1
    turtle.fd(30 * scale)
    turtle.left(90)
    turtle.fd(25 * scale)
    turtle.left(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(-80 * scale, 90)
    turtle.right(90)
    turtle.circle(-80 * scale, 90)
    turtle.end_fill()
    turtle.right(135)
    turtle.fd(60 * scale)
    turtle.left(180)
    turtle.fd(85 * scale)
    turtle.left(90)
    turtle.fd(80 * scale)
    
    # Leaves 2
    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(80 * scale, 90)
    turtle.left(90)
    turtle.circle(80 * scale, 90)
    turtle.end_fill()
    turtle.left(135)
    turtle.fd(60 * scale)
    turtle.left(180)
    turtle.fd(60 * scale)
    turtle.right(90)
    turtle.circle(200 * scale, 60)

def draw_tulip(color, scale=1.0):
    draw_rose(color, scale)

def draw_sunflower(color, scale=1.0):
    draw_rose(color, scale)

def draw_iris(color, scale=1.0):
    draw_rose(color, scale)

def draw_peony(color, scale=1.0):
    draw_rose(color, scale)

def draw_flowers_in_row(flower_functions, counts, colors):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()

    total_flowers = sum(counts)
    flower_width = (SCREEN_WIDTH - 2 * MARGIN) / total_flowers
    scales = [flower_width / 100 for _ in flower_functions]
    
    # Adjust distance between flowers based on the total number of flowers
    available_space = 1200 - 2 * MARGIN
    spacing = max((available_space - total_flowers * flower_width) / (total_flowers - 1), 5)

    x = -SCREEN_WIDTH / 2 + MARGIN

    for func, count, color, scale in zip(flower_functions, counts, colors, scales):
        for _ in range(count):
            turtle.goto(x, 0)  
            turtle.pendown()
            func(color, scale=scale)
            turtle.penup()
            x += spacing

def parse_input_and_draw(prompt):
    flowers = {"roses": "red", "tulips": "blue", "sunflowers": "yellow", "iris": "purple", "peonies": "pink"}
    number_pattern = r"\b\d+\b" 
    found_counts = {"roses": 0, "tulips": 0, "sunflowers": 0, "iris": 0, "peonies": 0}

    prompt = prompt.lower().translate(str.maketrans('', '', string.punctuation))

    for flower_name in flowers:
        pattern_number_flower = fr"({number_pattern})\s*({flower_name})"
        matches = re.findall(pattern_number_flower, prompt)
        
        for match in matches:
            number = int(match[0])
            found_counts[flower_name] += number

    flower_functions = [draw_rose, draw_tulip, draw_sunflower, draw_iris, draw_peony]
    colors = [flowers["roses"], flowers["tulips"], flowers["sunflowers"], flowers["iris"], flowers["peonies"]]
    counts = [found_counts["roses"], found_counts["tulips"], found_counts["sunflowers"], found_counts["iris"], found_counts["peonies"]]

    if any(counts):
        turtle.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        turtle.bgcolor("white")
        draw_flowers_in_row(flower_functions, counts, colors)
        turtle.done()
    else:
        print("No flowers found")

# User input example
prompt = input("Enter a prompt (e.g., '3 roses and 4 tulips'): ")
parse_input_and_draw(prompt)

