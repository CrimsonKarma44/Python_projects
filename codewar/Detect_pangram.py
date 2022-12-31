"""A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation."""

def is_pangram(s):
    count = 0
    for i in range(97, 123):
        if chr(i) in s.lower():
            count+=1
        else:
            count-=1
    if count == 26:
        return True
    else:
        return False
