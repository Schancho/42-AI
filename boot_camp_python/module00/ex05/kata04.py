t = ( 7, 15, 132411.222, 10000, 1.234567)

arg  = ""
arg += "module_" + str(t[0]).zfill(2) + ", "
arg += "ex_" + str(t[1]).zfill(2) + " : "
arg += str(format(t[2], ".2f")) + ", "
arg += str(format(t[3], "4.2e")) + ", "
arg += str(format(t[4], "4.2e"))
print(arg)