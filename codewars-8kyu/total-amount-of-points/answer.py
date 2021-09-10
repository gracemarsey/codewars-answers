def points(games):
    sum_points = 0
    for i in games:
        s = i.split(':')
        if s[0] > s[1]:
            sum_points += 3
        elif s[0] < s[1]:
            sum_points += 0
        elif s[0] == s[1]:
            sum_points += 1
    return sum_points