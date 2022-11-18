temptxt = "back"

sortedtxt = ''.join(sorted(temptxt))

dictionaryIndex = dict()

for i, c in enumerate(sortedtxt):
    dictionaryIndex.update({c: i})

columnOrder = []

for char in temptxt:
    columnOrder.append(dictionaryIndex.get(char))

print(f"Dict Index: {dictionaryIndex}")

print(f"Column order: {columnOrder}")

print(f"Alphabetic index: {sortedtxt}")