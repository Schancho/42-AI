import sys
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

args = sys.argv[1:]
string = ""
j = 0
for i in args:
    if j != len(args) - 1:
        string += i + " "
    else:
        string += i
    j += 1
result = string.split(' ')
j = 0
char = ""
for res in result:
    if not res.isalnum() and j != len(result) - 1:
        print("ERROR")
        exit(1)
    for i in res:
        char += MORSE_CODE_DICT[i.upper()]
    if j != len(result) - 1 :
        char += "/"
    j += 1
print(char)