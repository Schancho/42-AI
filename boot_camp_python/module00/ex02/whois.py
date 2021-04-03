import sys

args = sys.argv
if len(args) != 2 or  not (args[1].isdigit()):
    print("ERROR")
    exit(0)
integer = int(args[1])
if integer % 2 == 0:
    print("I'm Even.")
elif integer % 2 != 0:
    print("I'm Odd.")
elif integer == 0:
    print("I'm Zero.")