import time
import functools

def CreateFunctionWithWrapper(func):
    
    def func_with_wrapper(*args, **kwargs):
        start = time.time()        
        result = func(*args, **kwargs)
        end = time.time()
        print(">>>>>Function {} executed in {}".format(func.__name__, start - end))
        return result
    return func_with_wrapper



@CreateFunctionWithWrapper
def get_sequence(n):
    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v
    
print(get_sequence(19))


        
