import turtle

class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    
    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height
    
    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)

class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fill_color):
        super().__init__(x1, y1, width, height, color)
        self.fill_color = fill_color
    
    def draw_action(self):
        turtle.fillcolor(self.fill_color)
        turtle.begin_fill()
        super().draw_action()
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius
    
    def draw_action(self):
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self, x1, y1, radius, color, fill_color):
        super().__init__(x1, y1, radius, color)
        self.fill_color = fill_color
    
    def draw_action(self):
        turtle.fillcolor(self.fill_color)
        turtle.begin_fill()
        super().draw_action()
        turtle.end_fill()

p = Point(-100, 100, "blue")
p.draw()

b = Box(-100, 100, 50, 20, "blue")
b.draw()

bf = BoxFilled(1, 2, 100, 200, "red", "blue")
bf.draw()

c = Circle(50, -50, 30, "green")
c.draw()

cf = CircleFilled(-50, -50, 30, "orange", "yellow")
cf.draw()

turtle.done()
