# First Solution 

def disemvowel(string_):
    return string_.translate(str.maketrans("", "", "aeiouAEIOU"))

# Second Solution 

def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s