import time
import timeit

cpdef myfunc(int maxrange):
    cdef unsigned long long int total
    cdef long long int k
    cdef float t1, t2, t
    total = 0
    t1 = time.time()
    for k in range(maxrange):
        total = total + k
    print("Total =", total)
    t2 = time.time()
    t = t2-t1
    print("%.100f" % t)