import shelve

shelfFile = shelve.open("mydata")
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open("mydata")
dogs = ['Pansy', 'Grape']
shelfFile['dogs'] = dogs
shelfFile.close()

shelfFile = shelve.open("mydata")
print(type(shelfFile))  # <class 'shelve.DbfilenameShelf'>
print(shelfFile['cats'])  # ['Zophie', 'Pooka', 'Simon']
print(shelfFile['dogs'])  # ['Pansy', 'Grape']
shelfFile.close()

shelfFile = shelve.open("mydata")
print(list(shelfFile.keys()))  # ['cats', 'dogs']
print(list(shelfFile.values()))  # [['Zophie', 'Pooka', 'Simon'], ['Pansy', 'Grape']]
shelfFile.close()
