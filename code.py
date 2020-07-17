def decode(s):
    start = 0
    word_decoded = ""
    for c in s:
        if c.isdigit():
            start = s.index(c) + 1
            index = start + int(c)
            word_decoded = word_decoded + s[index]
    return word_decoded

print(decode("0h1ae2bcy"))
print(decode("2abh"))
print(decode("0b"))
