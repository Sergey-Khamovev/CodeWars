"""
You are given three integer inputs: length, minimum, and maximum.
Return a string that:
Starts at minimum
Ascends one at a time until reaching the maximum, then
Decends one at a time until reaching the minimum
repeat until the string is the appropriate length
Examples:
 length: 5, minimum: 1, maximum: 3   ==>  "123 21"
 length: 14, minimum: 0, maximum: 2  ==>  "012 10 12 10 12 10 1"   012 10 12 10 12 10 12
 length: 33, minimum: 5, maximum: 9  ==>  "56789 8765 6789 8765 6789 8765 6789 8765"
Notes:
length will always be non-negative
negative numbers can appear for minimum and maximum values
hyphens/dashes ("-") for negative numbers do count towards the length
the resulting string must be truncated to the exact length provided
return an empty string if maximum < minimum or length == 0
minimum and maximum can equal one another and result in a single number repeated for the length of the string
"""
def ascend_descend(length, minimum, maximum):
    if minimum == maximum:
        return "".join(str(minimum)*length)[:length]
    temp = [str(i) for i in range(minimum, maximum + 1)]
    forw, revers = temp[1:], temp[-2::-1]
    flag = True
    for i in range(length):
        if flag:
            temp.extend(revers)
            flag = False
        else:
            temp.extend(forw)
            flag = True
    return "".join(str(i) for i in temp)[:length]







