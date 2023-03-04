import time
import functools

@functools.lru_cache(maxsize=100)
def fib(n):
        
    if n < 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
            
    return result

start = time.time()
for x in range(35):
    result = fib(x)
    print("Number in fib {} = {}, time spent on counting {}".format(x, result, time.time() - start))

result = time.time() - start

print(fib.cache_info())

          

                                                              