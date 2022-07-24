"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet
should be shifted, like in the original Rot13 "implementation".
"""
def rot13(message):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "".join(i.capitalize() for i in lower_alphabet)
    res = ""
    for i in range(len(message)):
        if message[i] in lower_alphabet:
            index = lower_alphabet.index(message[i]) + 13
            res += lower_alphabet[index] if index < 26 else lower_alphabet[index%26]
        elif message[i] in upper_alphabet:
            index = upper_alphabet.index(message[i]) + 13
            res += upper_alphabet[index] if index < 26 else upper_alphabet[index%26]
        else:
            res += message[i]
    return res

def test_rot13(func):
    assert rot13("Hello!") == "Uryyb!", "Должно быть  'Uryyb!' "
    assert rot13("Hi") == "Uv", "Должно быть  'Uv' "
    assert rot13("Sergey") == "Fretrl", "Должно быть  'Fretrl' "
test_rot13(rot13)