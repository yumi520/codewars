# Multiples of 3 or 5
# kyu 6


def solution(number):
    counter = 0
    if number < 0:
        return 0
    
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            counter += x
    return counter