def print_lol(the_list, indent = False, level = 0):
    '''此函数将递归地打印列表中的每个元素
        第一个参数the_list为要打印的列表
        第二个参数indent决定打印列表及嵌套列表时是否要缩进及额外缩进，默认不缩进
        第三个参数level设定缩进值，默认不缩进'''
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item, indent, level+1)
        else:
            if indent:
                for tab_step in range(level):
                    print('\t', end = '')
            print(each_item)

name = [1,2,3,[4,5,6,[7,8,9]]]
print_lol(name)
print_lol(name,True)
print_lol(name,True,2)



