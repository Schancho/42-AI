
t = (19,42,21)
l = len(t)
k = ""
for i in t:
    if l != 1:
        k += str(i) + ", "
    l -= 1
k += str(i)
print("The 3 numbers are: " + k)