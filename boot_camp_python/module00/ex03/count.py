import string
""" This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
def text_analyzer(*text):
    """     
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if len(text) > 1:
        print("ERROR")
        exit (0)
    l = 0
    u = 0
    p = 0
    s = 0
    total = 0
    for i in text:
        if i.islower():
            l += 1
        elif i.isupper():
            u += 1
        elif i in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            p += 1
        elif i == ' ':
            s += 1
        else:
            total += 1
    total = total + s + p + u + l
    print("The text contains " +  str(total) + " characters:")
    print("- " + str(u) + " upper letters")
    print("- " + str(l) + " upper letters")
    print("- " + str(p) + " punctuation marks")
    print("- " + str(s) + " spaces")

print(text_analyzer.__doc__)
    
