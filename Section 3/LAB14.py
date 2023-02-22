import time, math

formulas_list = ["abs(x**3 - x**0.5)",
                "abs(math.sin(x) * x**2)"]
    
argument_list = []

for i in range (100000):
    argument_list.append(i/10)
for j in formulas_list:
    results_list = []
    print(j)
    start = time.time()
    for x in argument_list:
        results_list.append(eval(j))
    stop = time.time()
    print()
    print("Min:",min(results_list), "Max:", max(results_list))
    print("Time counting formula:", stop - start)

for i in range (100000):
    argument_list.append(i/10)
for j in formulas_list:
    sourceCompiled = compile(j, j, 'eval')
    start = time.time()
    for x in argument_list:
        results_list.append(eval(sourceCompiled))
    stop = time.time()
    print("Po kompilacji")
    print("Min:",min(results_list), "Max:", max(results_list))
    print("Time counting formula:", stop - start)

# print(results_list)


