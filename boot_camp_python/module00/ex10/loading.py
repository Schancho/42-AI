import time
import sys

x = 1
def ft_progress(lst):
    global x
    for l in range(0,lst,10):
        sys.stdout.write('\b')
        print("=>" * x,end='')#, flush=True)
        yield l
    x += 1
listy = 1000 
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)