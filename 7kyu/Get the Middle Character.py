"""
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd,
return the middle character. If the word's length is even,
return the middle 2 characters.
#Examples:
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"
"""
def get_middle(s):
    if len(s) % 2 != 0 and len(s) < 2:
        return s
    if len(s) % 2 == 0 and len(s) == 2:
        return s
    return get_middle(s[1:-1])


firstString = "abcdefghijklmnopqrstuvwxyz"
secondString = "ijklmnopqrstuvwxyzabcdefgh"
myword = "abcdefgh"
ts = myword.maketrans(firstString, secondString)
print(myword.translate(ts))
