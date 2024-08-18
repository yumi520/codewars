# 7 kyu
# Sum of a sequence

def sequence_sum(begin_number, end_number, step):
    if begin_number == end_number and begin_number == step:
        return begin_number
    
    if begin_number > end_number:
        return 0
    
    return sum(range(begin_number, end_number + 1, step))

# range has a built-in (begin, end, step)