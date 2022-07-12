"""
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
"Should return 5 for \"abracadabra\""
Should return 0 for empty string
Should return 0 when no vowels
"""


def get_count(sentence):
    return sum(1 for i in sentence if i in "aeiou")
