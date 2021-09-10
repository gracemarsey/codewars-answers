def fake_bin(number_string):
    binary_string=""
    for x in number_string:
        if int(x) < 5:
            binary_string += '0'
        else:
            binary_string += '1'
    return binary_string