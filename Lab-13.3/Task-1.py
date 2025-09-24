from math import pi

def calculate_area(shape, *args):
    shape = shape.lower()
    if shape == "rectangle":
        if len(args) != 2:
            return "Rectangle requires 2 arguments (length, width)"
        length, width = args
        return length * width
    elif shape == "square":
        if len(args) != 1:
            return "Square requires 1 argument (side length)"
        side, = args
        return side * side
    elif shape == "circle":
        if len(args) != 1:
            return "Circle requires 1 argument (radius)"
        radius, = args
        return pi * radius * radius
    else:
        return "Unknown shape"
if __name__ == "__main__":
    print("Area of rectangle (5, 10):", calculate_area("rectangle", 5, 10))  
    print("Area of square (4):", calculate_area("square", 4))               
    print("Area of circle (3):", calculate_area("circle", 3))               
    print("Area of unknown shape:", calculate_area("triangle", 5, 10))