tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def find_width(list_of_strings):
    width= 0
    for x in list_of_strings:
        if type(x) != str:
            print(f'{x} is not a string, therefore we can not proceed.')
            return -1
        else:
            if len(x)> width:
                width = len(x)
            else:
                continue
    return width

def find_table_width(table):
    col_width = [0] * len(table)
    for i in range(len(col_width)):
        if find_width(table[i])>=0:
            col_width[i] = find_width(table[i])
        else:
            break
    return col_width

def format_table(table):
    col_width = find_table_width(table)
    depth = len(table[0])
    table_format = []
    for j in range(depth):
        new_item=''
        for i in range(len(table)):
            new_item+=' '+table[i][j].ljust(col_width[i])
        table_format.append(new_item)
    return table_format

def print_table(table):
    for i in table:
        print(i)

print_table(format_table(tableData))