def collatz(number):
    print(number)
    if number % 2 == 0:
        collatz(number // 2)
        # return number // 2
    elif number % 2 == 1 and number > 1:
        collatz(3 * number + 1)
        # return 3 * number + 1

try:
    str_num = input("请输入一个整数：")
    str_num = int(str_num)
    collatz(str_num)
except ValueError as err:
    print("Exception：", err)
