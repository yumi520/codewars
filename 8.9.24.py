# 6 kyu
# Split Strings

def solution(s):
    
    if len(s) == 0:
        return []
    
    if len(s) % 2 != 0:
        s += "_"
    
    return [s[i:i+2] for i in range(0, len(s), 2)]

# checking if the length is 0, its an empty array
# if it is not even, we can add an underscore to the end of s
# for i in range(0, len(s), 2) means start at 0, end at the length of the stringm, and increment by 2s
# s[i:i+2] is splinting
# s = "abcdef"
# When i = 0, s[i:i+2] gives "ab".
# When i = 2, s[i:i+2] gives "cd".
# When i = 4, s[i:i+2] gives "ef".