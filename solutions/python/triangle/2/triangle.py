def is_triangle(sides):
    a,b,c = sides
    return (a + b >= c and a + c >= b and b + c >= a) and sum(sides) != 0
    
def equilateral(sides):
    a,b,c = sides
    
    return a == b == c and is_triangle(sides)


def isosceles(sides):
    a,b,c = sides
    return len(set(sides)) <= 2 and is_triangle(sides)


def scalene(sides):
    a,b,c = sides
    return a != b and a != c and b != c and is_triangle(sides)