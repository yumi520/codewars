# My Language Skills
# 7 kyu

def my_languages(results):
    test_scores = []
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    
    for keys, values in sorted_results:
        if values >= 60:
             test_scores.append((keys))
            
            
    return test_scores

# to get the keys and values in the tuples, i was able to use results.items() which returns all the tuples
# I looked up how I can sort tuples
# it basically is getting the tuples, using a lambda function to get the second element
# put reverse = true, so it sorts from highest to lowest
# then if it is >= 60, I can append it to the empty array

# key=lambda is basically just telling sorted() to use the function