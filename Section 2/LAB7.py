

def returningColors( colors, numberOfColors) -> list:
    # newColors = colors[:numberOfColors]
    # print(id(colors), id(newColors))
    # return newColors
    return colors[:numberOfColors]

colors = ["red", "orange", "green", "violet", "blue", "yellow"]

# print(returningColors(colors, 2))

for list in range(1,len(colors)+1):
    print(returningColors(colors, list))

text = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '
print(text[text.index('(') + 1: text.index(')')])