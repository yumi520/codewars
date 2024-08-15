# 7 kyu
# Highest and Lowest

def high_and_low(numbers):
    nums_array = []
    for n in numbers.split(" "):
        nums_array.append(int(n))
    nums_array.sort()
    return str(nums_array[len(nums_array) - 1]) + " " + str(nums_array[0])


# The numbers came in a string divided up by spaces so first I 
# used a for loop to get each element and split the spaces (careful not to also get rid of the negative signs)
# then I added to an empty array but also converting it to an int
# I then sort it and formatted it in "highest lowest"