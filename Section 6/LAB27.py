class Cake:
    def __init__(self, name, kind, taste, addititives, filling) -> None:
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = addititives.copy()
        self.filling = filling


cake1 = Cake('Cheese cake', 'cake', 'vanilla', ['chocolade','nuts'], 'cream')
cake2 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake3 = Cake('Super Sweet Maringue', 'meringue', 'very sweet ', [''], '')

cakes = [cake1, cake2, cake3]

print("Today in our offer:")
for c in cakes:
    print("{} - ({}) main taste: {} with additives of {}, filled with {}".format(
        c.name, c.kind, c.taste, c.additives, c.filling))