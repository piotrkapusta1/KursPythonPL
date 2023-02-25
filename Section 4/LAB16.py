
# ZAD 1

def calculate_paint(efficency_ltr_per_m2, *args) -> float:
    suma = 0
    for x in args:
        suma += (efficency_ltr_per_m2 * x)
    return suma

print(calculate_paint(10.0,10,20,40))
rooms = [10,20,30,40]
print(calculate_paint(10.0, *rooms))

# ZAD 2

def log_it(*args):
    with open(r"/home/piotr/Documents/VS Program/KursPythonPL/KursPythonPL/Section 4/log_it.txt", 'a') as f:
        for x in args:
            f.write(x + " ")
        f.write("\n")

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')