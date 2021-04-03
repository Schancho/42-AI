import sys

args = sys.argv[::-1]
args.pop()
text = ""
for i in args:
    i = i[::-1]
    text += i
    if i != args[-1] and i != "":
        text += " "
text = text[:-1]
string = ""
for j in text:
    if j.isupper() == True:
        string += j.lower()
    elif j.islower() == True:
        string += j.upper()
    else:
        string += ' '
print(string)