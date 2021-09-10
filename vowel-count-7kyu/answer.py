# First solution
def get_count(sentence):
    count = 0
    for x in sentence:
        if x == "a":
            count = count + 1
        elif x == "e":
            count = count + 1
        elif x == "i":
            count = count + 1
        elif x == "o":
            count = count + 1
        elif x == "u":
            count = count + 1
    return count

# Second more concise solution
def get_count(sentence):
    count = 0
    for x in sentence:
        if x in "aeiou":
            count = count +1
    return count

