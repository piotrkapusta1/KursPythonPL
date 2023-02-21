import time, math
formulas_list = "abs(x**3 - x**0.5)"
    

argument_list = []
x = 1.5
exec(formulas_list)
print(x)
print(formulas_list)
# for i in range (1000000):
#     argument_list.append(i/10)
# for j in formulas_list:
#     results_list = []
#     print(j)
#     x = 1
#     exec(j)
#     print(x)
    
    
    # print("Min:", min(results_list), "Max:" , max(results_list))