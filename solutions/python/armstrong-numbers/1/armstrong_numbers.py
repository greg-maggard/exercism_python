def is_armstrong_number(number):
    digits = str(number)
    final_sum = 0
    exponent = len(digits)
    for digit in digits:
        final_sum += int(digit) ** exponent
    return final_sum == number
    
    