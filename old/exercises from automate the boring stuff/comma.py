def comma_and(list):
    if list:
        list.insert(-1, 'and')
        for x in list[:-1]:
            print(x, end=', ')
        print(list[-1])
    else:
        pass
eggs=['apples', 'bananas', 'tofu', 'cats', []]
comma_and(eggs)
comma_and([])