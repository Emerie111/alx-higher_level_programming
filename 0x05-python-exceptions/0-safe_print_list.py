def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while i < 0:
            print(my_list[i], end='')
            i = i + 1
        print()
    except:
        print()
    return i
