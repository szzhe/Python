# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name]  # list concatenation
# print('The cat names are:')
# for name in catNames:
#     print(' ' + name)

''' 第3章，函数，实践项目 '''

# def collatz(number):
#     print(number)
#     if number == 1:
#         return
#     elif number % 2 == 0:
#         num = number // 2
#         collatz(num)
#     elif number % 2 == 1:
#         num = 3 * number + 1
#         collatz(num)

# try:
#     str_num = input("Please input one number: ")
#     str_num = int(str_num)
#     collatz(str_num)
# except ValueError as err:
#     print("Except", err)

''' 第4章，列表，实践项目，逗号代码 '''

# def test(str_list):
#     result = []
#     for i in range(len(str_list)):
#         if i == len(str_list) - 1:
#             str_list[i] = "and" + " " + str_list[i]
#         result.append(str_list[i])
#         result_str = ",".join(result)
#     return result_str
#
# spam = ['apples', 'bananas', 'tofu', 'cats']
# print((str(test(spam))))

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')

''' dict.get(self, k, default) '''
# picnicItems = {'apples': 5, 'cups': 2}
# print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
# print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

''' dict.setdefault(self, k, default) '''
# spam = {'name': 'Pooka', 'age': 5}
# spam.setdefault('color', 'black')  # black
# print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}
# spam.setdefault('color', 'white')  # black
# print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}

''' 计算一个字符串中每个字符出现的次数 '''
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
#
# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1
# print(count)

# 漂亮打印

# from pprint import pprint, pformat
#
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
#
# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1
# pprint(count)  # 想要字典中表项的显示比 print()的输出结果更干净
# # pprint(pformat(count))  # 希望得到漂亮打印的文本作为字符串， 而不是显示在屏幕上

''' 第5章 井子键盘 '''
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
#
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#
# turn = "X"
#
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == "X":
#         turn = "O"
#     else:
#         turn == "X"
#
# printBoard(theBoard)

''' 嵌套的字典和列表,用于记录谁为野餐带来了什么食物 '''
# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
#              'Bob': {'ham sandwiches': 3, 'apples': 2},
#              'Carol': {'cups': 3, 'apple pies': 1}}
#
# def totalBrought(guests, item):
#     numBrought = 0
#     for k, v in guests.items():
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought
#
# print('Number of things being brought:')
# print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
# print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
# print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
# print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
# print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))

''' 第5章 实践项目 '''

def displayInventory(inventory):
    item_total = 0
    print("inventory: ")
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print("Total number of items: ", item_total)

# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# displayInventory(stuff)

def addToInventory(inventory, addedItems):
    new_item = {}

    for x in addedItems:
        new_item[x] = addedItems.count(x)  # {'gold coin': 3, 'dagger': 1, 'ruby': 1}

    for k, v in new_item.items():
        if k in inventory.keys():
            new_item[k] = inventory[k] + v  # {'gold coin': 45, 'dagger': 1, 'ruby': 1}

    for k, v in inventory.items():
        if k not in new_item.keys():
            new_item[k] = inventory[k]

    # print(new_item)
    return new_item

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
