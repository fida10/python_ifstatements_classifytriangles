""" 
Practice Question 3: Classify Triangles

Task:

Write a function classify_triangle that takes 
three integers representing the sides of a triangle. 
The function should return the type of the triangle 
('Equilateral', 'Isosceles', 'Scalene', or 'Not a triangle').
"""
def is_a_triangle(x, y, z):
    return x + y > z and y + z > x and x + z > y and x * y * z > 0

def classify_triangle(x, y, z):
    if not is_a_triangle(x, y, z):
        return 'Not a triangle'

    set_of_sides = {x, y, z}
    if(len(set_of_sides) == 1):
        return 'Equilateral'
    elif(len(set_of_sides) == 2):
        return 'Isosceles'
    else:
        return 'Scalene'