tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


# 要求输出如下：
#   apples   Alice    dogs
#  oranges     Bob    cats
# cherries   Carol   moose
#   banana   David   goose

def printTable(data):
    str_data = ''
    col_len = []
    for row in range(0, len(data[0])):  # row=4
        for col in range(0, len(data)):  # col=3
            col_len.append(len(data[col][row]))
    max_col_len = max(col_len)
    print("列表各元素长度为：", col_len)
    print("列表中最大值为：", max_col_len)  # 8
    for row in range(0, len(data[0])):
        for col in range(0, len(data)):
            print(data[col][row].rjust(max_col_len), end='')
        print()

    return str_data


f_data = printTable(tableData)
print(f_data)
