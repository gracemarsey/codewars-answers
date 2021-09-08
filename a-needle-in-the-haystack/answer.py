def find_needle(haystack):
    for x in haystack:
        if x == str("needle"):
            return "found the needle at position {}".format(haystack.index(x))