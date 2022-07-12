"""
Given a mixed array of number and string representations of integers, add up the string integers and subtract this from
the total of the non-string integers. Return as a number.
test.assert_equals(div_con([9, 3, '7', '3']), 2)
"""
def div_con(x):
    sumint = [each for each in x if isinstance(each, int)]
    sumstr = [int(each) for each in x if isinstance(each, str)]
    return sum(sumint) - sum(sumstr)
