
import pyperclip

'''
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
'''

text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
print(text)