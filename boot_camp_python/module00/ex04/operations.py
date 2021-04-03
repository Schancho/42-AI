import sys

args = sys.argv

num_of_arg = len(args)
if num_of_arg < 3:
    print("Usage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3")
elif num_of_arg > 3:
    print("InputError: too many arguments\n")
    print("Usage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3")
elif not args[1].isdigit() or not args[2].isdigit():
    print("InputError: only numbers\n")
    print("Usage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3")
else:
    print("Sum:         " + str(int(args[1]) + int(args[2])))
    print("Difference:  " + str(int(args[1]) - int(args[2])))
    print("product:     " + str(int(args[1]) * int(args[2])))
    if int(args[2]) != 0:
        print("Quotient:    " + str(int(args[1]) / int(args[2])))
    else:
        print("Quotient:    EROOR (div by zero)")
    if int(args[2]) != 0:
        print("Remainder:   " + str(int(args[1]) % int(args[2])))
    else:
        print("Remainder:   EROOR (modulo  by zero)")
    