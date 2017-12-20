import pyperclip, shelve

madShelf = shelve.open("mad")
text = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events"
lines = text.split()

madShelf["lines"] = lines
# print(list(madShelf.keys()))
# print(list(madShelf.values()))
# print(lines)



text = " ".join(lines)
print(text)

madShelf.close()


