def max_min(lst):
    highest = 0
    lowest = 0
    for i in lst:
        if i > highest:
            highest = i
        if i < lowest:
            lowest = i
    return [lowest, highest]


print(max_min([2, 4, 1, 0, 2, -1]))
