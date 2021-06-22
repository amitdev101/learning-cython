import time
def myfunc(maxrange):
    total=0
    t1 = time.time()
    for k in range(maxrange):
        total = total + k
    print("Total =", total)
    t2 = time.time()
    t = t2-t1
    print("%.100f" % t)