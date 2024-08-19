# 7 kyu
# Some (but not all)

def some_but_not_all(seq, pred): 
    result = list(map(pred, seq))
    return any(result) and not all(result)

# simpler version
def some_but_not_all(seq, pred):
    results = map(pred, seq)
    has_true = False
    all_true = True

    for result in results:
        if result:
            has_true = True
        if not result:
            all_true = False

    return has_true and not all_true

# For the sequence [1, 1] and predicate x > 3:

# Predicate results: [False, False]
# has_true: False (no elements are greater than 3)
# all_true: False (since no elements are True)
# Result: False (no elements satisfy the predicate)

