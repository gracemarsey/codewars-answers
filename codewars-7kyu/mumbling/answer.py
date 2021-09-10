# First solution 
def accum(s):
    result = []
    for i in range(len(s)):
        upper_case= s[i].upper()
    
        for v in range(i):
            upper_case += s[i].lower()
    
        result.append(upper_case)

    return "-".join(result)

# Second solution 

def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))