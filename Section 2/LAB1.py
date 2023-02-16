a = b = c = 10

print("Zmienna a = ", a, id(a))
print("Zmienna b = ", b, id(b))
print("Zmienna c = ", c, id(c))
print("-----------------------------")

a = 20
print("Zmienna a = ", a, id(a))
print("Zmienna b = ", b, id(b))
print("Zmienna c = ", c, id(c))

d = e = f = [1,2,3]

d.append(4)
print("Zmienna d = ", d, id(d))
print("Zmienna e = ", e, id(e))
print("Zmienna f = ", f, id(f))

x = 10
y = 10

print("Zmienna x = ", x, id(x))
print("Zmienna y = ", y, id(y))
print("-----------------------------")

y = y + 1 - 1
print("Zmienna x = ", x, id(x))
print("Zmienna y = ", y, id(y))
print("-----------------------------")

y = y + 1234567890 - 1234567890
print("Zmienna x = ", x, id(x))
print("Zmienna y = ", y, id(y))



