# import math
# argument_list = [x*0.1 for x in range(0,100)]
# print(argument_list)
# formula = input("Input formula: ")
# for x in argument_list:
#     result = eval(formula)
#     print(result)

import math
     
argument_list = []
     
for i in range (100):
    argument_list.append(i/10)
        
formula = input("Please enter a formula, use 'x' as the argument: ")
     
for x in argument_list:
    print("{0:3.1f} {1:6.2f}".format(x, eval(formula)))