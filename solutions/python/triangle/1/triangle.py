def equilateral(sides):
    a,b,c = sides
    
    return a == b == c and (a + b >= c and a + c >= b and b + c >= a) and sum(sides) != 0


def isosceles(sides):
    a,b,c = sides
    return len(set(sides)) <= 2 and (a + b >= c and a + c >= b and b + c >= a) and sum(sides) != 0


def scalene(sides):
    a,b,c = sides
    return a != b and a != c and b != c and (a + b >= c and a + c >= b and b + c >= a) and sum(sides) != 0