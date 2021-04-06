import sys
import string

args = sys.argv
if len(args) != 3 or args[1].isdigit() or not args[2].isdigit():
    print("ERROR")
    exit(1)
arg = args[1].split()
string = ""
sublist = ""
for ar in arg:
    for letter in ar:
        if not (letter in string.punctuation):
            sublist += letter
    string.append(sublist)
    sublist = ""
print(string)