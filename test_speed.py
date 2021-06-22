import hellocy
import hellopy
import timeit

maxrange = 10**7
# hellocy.myfunc(maxrange)
# hellopy.myfunc(maxrange)

number = 5
t1 = timeit.Timer(lambda:hellocy.myfunc(maxrange))
t1.timeit(number=number)

# t2 = timeit.Timer(lambda:hellopy.myfunc(maxrange))
# t2.timeit(number=number)


