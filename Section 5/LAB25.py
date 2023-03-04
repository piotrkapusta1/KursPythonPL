text_list = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda text: len(text)

print(str(f('tekst')))

print(list(map(f, text_list)))

print(list(map(lambda text: len(text), text_list)))
