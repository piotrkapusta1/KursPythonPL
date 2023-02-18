import os

def countWords(path) -> int:
    f = (open(path, "r")).read()
    return len(f.split())


path = r"/home/piotr/Documents/VS Program/KursPythonPL/KursPythonPL/Section 2/textToLAB4.txt"

if os.path.isfile(path):
    words = countWords(path)
    print("String has",words, "words")

result = os.path.isfile(path) and countWords(path)
print("String has",result, "words")