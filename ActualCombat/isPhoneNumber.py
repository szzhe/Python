import re


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():  # 数字，非空
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

'''------------------------search()方法-------------------------------'''

'''
1．用import re 导入正则表达式模块。
2．用re.compile()函数创建一个Regex 对象（记得使用原始字符串）。
3．向Regex 对象的search()方法传入想查找的字符串。它返回一个Match 对象。
4．调用Match 对象的group()方法，返回实际匹配文本的字符串。
'''
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

phoneNumRegex1 = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo1 = phoneNumRegex1.search('My number is 415-555-4242.')

print('Phone number found: ' + mo1.group(1))  # Phone number found: 415
print('Phone number found: ' + mo1.group(2))  # Phone number found: 555-4242
print('Phone number found: ' + mo1.group())  # Phone number found: 415-555-4242
print('Phone number found: ' + mo1.group(0))  # Phone number found: 415-555-4242

print(mo1.groups())  # ('415', '555-424')
areaCode, mainNumber = mo1.groups()
print(areaCode)  # 415
print(mainNumber)  # 555-424

phoneNumRegex2 = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo2 = phoneNumRegex2.search('My phone number is (416) 555-4242.')
print(mo2.groups())  # ('(416)', '555-4242')

phoneNumRegex3 = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = phoneNumRegex3.search('Batmobile lost a wheel')
print(mo3.group())  # 返回了完全匹配的文本'Batmobile'
print(mo3.group(1))  # 返回第一个括号分组内匹配的文本'mobile'

batRegex = re.compile(r'Bat(wo)?man')  # 不论这段文本在不在，正则表达式都会认为匹配
mo4 = batRegex.search('The Adventures of Batman')
print(mo4.group())  # Batman
mo5 = batRegex.search('The Adventures of Batwoman')
print(mo5.group())  # Batwoman

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo6 = phoneRegex.search('My number is 415-555-4242')
print(mo6.group())  # 415-555-4242
mo7 = phoneRegex.search('My number is 555-4242')
print(mo7.group())  # 555-4242

batRegex1 = re.compile(r'Bat(wo)*man')  # 正则表达式的(wo)*部分匹配wo的零次或多次”
mo8 = batRegex1.search('The Adventures of Batman')
print(mo8.group())  # Batman
mo9 = batRegex1.search('The Adventures of Batwoman')
print(mo9.group())  # Batwoman
mo10 = batRegex1.search('The Adventures of Batwowowowoman')
print(mo10.group())  # Batwowowowoman

batRegex2 = re.compile(r'Bat(wo)+man')  # 正则表达式的(wo)*部分匹配wo的零次或多次”
mo11 = batRegex2.search('The Adventures of Batwoman')
print(mo11.group())  # Batwoman
mo12 = batRegex2.search('The Adventures of Batwowowowoman')
print(mo12.group())  # Batwowowowoman
mo13 = batRegex2.search('The Adventures of Batman')
print(mo13 == None)  # True

haRegex = re.compile(r'(Ha){3,5}')  # (Ha){3,}将匹配3次或更多次实例，(Ha){,5}将匹配0到5次实例
mo1 = haRegex.search('HaHaHaHaHa')
print(mo1.group())  # HaHaHaHaHa
mo2 = haRegex.search('Ha')
print(mo2 == None)  # True

'''贪心和非贪心匹配'''
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())  # 'HaHaHaHaHa'

# 问号在正则表达式中可能有两种含义：声明非贪心匹配或表示可选的分组 Bat(wo)?man
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())  # 'HaHaHa'

'''---------------------------------findall()方法---------------------------------------------------------'''
# search()返回一个Match对象，包含被查找字符串中的“第一次”匹配的文本
# findall()不是返回一个Match 对象，而是返回一个字符串列表，只要在正则表达式中没有分组。
# 列表中的每个字符串都是一段被查找的文本，它匹配该正则表达式

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo1 = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1.group())  # 415-555-9999
print(mo2)  # ['415-555-9999', '212-555-0000'] 调用在一个没有分组的正则表达式上，返回一个匹配字符串的列表

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo3 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo3)  # [('415', '555', '9999'), ('212', '555', '0000')] 调用在一个有分组的正则表达式上，返回一个字符串的元组的列表

'''---------------------------------字符分类---------------------------------------------------------'''

'''
\d 0 到9 的任何数字
\D 除0 到9 的数字以外的任何字符
\w 任何字母、数字或下划线字符（可以认为是匹配“单词”字符）
\W 除字母、数字和下划线以外的任何字符
\s 空格、制表符或换行符（可以认为是匹配“空白”字符）
\S 除空格、制表符和换行符以外的任何字符
'''

xmasRegex = re.compile(r'\d+\s\w+')
mo1 = xmasRegex.findall(
    '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo1)
# ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '6 geese', '5 rings', \
# '4 birds', '3 hens', '2 doves', '1 partridge']

# 正则表达式\d+\s\w+匹配的文本有一个或多个数字(\d+)，接下来是一个空白字符(\s)，接下来是一个或多个字母/数字/下划线字符(\w+)

xmasRegex = re.compile(r'(\d+)(\s)(\w+)')
mo2 = xmasRegex.findall(
    '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo2)
# [('12', ' ', 'drummers'), ('11', ' ', 'pipers'), ('10', ' ', 'lords'), ('9', ' ', 'ladies'), ('8', ' ', 'maids'), ('6', ' ', 'geese'), ('5', ' ', 'rings'),\
#  ('4', ' ', 'birds'), ('3', ' ', 'hens'), ('2', ' ', 'doves'), ('1', ' ', 'partridge')]

'''用方括号定义自己的字符分类'''

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo1 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo1)  # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

# 使用短横表示字母或数字的范围[a-zA-Z0-9]
# 在方括号内，普通的正则表达式符号不会被解释。这意味着，你不需要前面加上倒斜杠转义.、*、?或()字符。错误案例：[0-5\.]

# 在字符分类的左方括号后加上一个插入字符（^），就可以得到“非字符类”。非字符类将匹配不在这个字符类中的所有字符
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo1 = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo1)  # ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

'''---------------------------------插入字符和美元字符---------------------------------------------------------'''

# 在正则表达式的开始处使用插入符号（^），表明匹配必须发生在被查找文本开始处
# 再正则表达式的末尾加上美元符号（$），表示该字符串必须以这个正则表达式的模式结束
# 可以同时使用^和$，表明整个字符串必须匹配该模式

beginsWithHello = re.compile(r'^Hello')
mo1 = beginsWithHello.search('Hello world!')
print(mo1.group())  # Hello
mo2 = beginsWithHello.search('He said hello.')
print(mo2 == None)  # True

endsWithNumber = re.compile(r'\d$')
mo1 = endsWithNumber.search('Your number is 42')
print(mo1.group())  # 2
endsWithNumber = re.compile(r'\d+$')
mo2 = endsWithNumber.search('Your number is 42')
print(mo2.group())  # 42
mo3 = endsWithNumber.search('Your number is forty two.')
print(mo3 == None)  # True

wholeStringIsNum = re.compile(r'^\d+$')
mo1 = wholeStringIsNum.search('1234567890')
print(mo1.group())  # 1234567890
mo2 = wholeStringIsNum.search('12345xyz67890')
print(mo2 == None)  # True
mo3 = wholeStringIsNum.search('12 34567890')
print(mo3 == None)  # True 必须匹配

'''---------------------------------通配字符---------------------------------------------------------'''

# .（句点）字符称为“通配符”.匹配除了换行之外的所有字符（只匹配一个字符）

atRegex = re.compile(r'.at')
mo1 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo1)  # ['cat', 'hat', 'sat', 'lat', 'mat']

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: A l Last Name: Sweigart')
print(mo.group())  # First Name: A l Last Name: Sweigart
print(mo.group(1))  # A l
print(mo.group(2))  # Sweigart

nongreedyRegex = re.compile(r'<.*?>')
mo1 = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo1.group())  # <To serve man>

nongreedyRegex = re.compile(r'<.*>')
mo2 = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo2.group())  # <To serve man> for dinner.>

'''字符串'<To serve man> for dinner.>'对右肩括号有两种可能的匹配。
在非贪心的正则表达式中，Python 匹配最短可能的字符串：'<To serve man>'。
在贪心版本中，Python 匹配最长可能的字符串：'<To serve man> for dinner.>'''

