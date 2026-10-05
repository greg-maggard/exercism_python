def square(number):
    if number >= 1 and number <= 64: 
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    square_values = []
    for i in range(64):
         square_values.append(2 ** i)
    return sum(square_values)        
