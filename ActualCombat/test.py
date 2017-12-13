# 九九乘法口诀表
# for x in range(1, 10):  # 1-9
#     for y in range(1, x + 1):
#         print("%d*%d=%d" % (x, y, x * y), end=" ")
#     print()

'''
*
* *
* * *
* * * *
* * * * *
'''

# for x in range(1, 6):
#     for y in range(1, x + 1):
#         print("*", end=" ")
#     print()

'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

# num = 6
# for x in range(1, num):
#     for y in range(num - x):
#         print("*", end=" ")
#     print()

'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''

# num = 5
# for x in range(1, num + 1):
#     for y in range(num - x):
#         print(" ", end=" ")
#     for y in range(x):
#         print("*", end=" ")
#     print()