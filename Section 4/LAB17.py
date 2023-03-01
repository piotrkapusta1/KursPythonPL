def double(x):
    return 2 *x
     
def square(x):
    return x**2
     
def negative(x):
    return -x
     
def div2(x):
    return x/2

number = 8
instructions = [double, square, div2, negative]
tmp_return_value = number

print('Starting transformations')
for function in instructions:
    tmp_return_value = function(tmp_return_value)
    print('{}: value= {}'.format(function.__name__, tmp_return_value))

instructions = [square, square, div2, double]
tmp_return_value = number

print('Starting transformations')
for function in instructions:
    tmp_return_value = function(tmp_return_value)
    print('{}: value= {}'.format(function.__name__, tmp_return_value))




