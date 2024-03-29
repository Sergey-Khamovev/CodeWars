"""
Task
Given a Divisor and a Bound , Find the largest integer N , Such That ,
Conditions :
N is divisible by divisor
N is less than or equal to bound
N is greater than 0.

Notes
The parameters (divisor, bound) passed to the function are only positive values .
It's guaranteed that a divisor is Found .

maxMultiple (10,50)  ==> return (50)
Explanation:
(50) is divisible by (10) , (50) is less than or equal to bound (50) , and (50) is > 0 .*

maxMultiple (37,200) ==> return (185)
Explanation:
(185) is divisible by (37) , (185) is less than or equal to bound (200) , and (185) is > 0 .
"""
def max_multiple(divisor, bound):
    for i in range(bound, divisor-1, -1):
        if (i % divisor == 0):
            return i

