from list_manager import add_item, remove_item


def main():
    lists = []
    while True:
        k = input('(A)Add, (R)remove, (V)view, (Q)quit: ').strip().lower()
        if k == 'a':
            item = input('Item to add: ')
            add_item(item, lists)
        elif k == 'r':
            item = input('Item to remove: ')
            remove_item(item, lists)
        elif k == 'v':
            print('Your Current list: ',lists if lists else 'Empty')
        elif k == 'q':
            break
        else:
            print('Please enter a, r, v or q')


if __name__ == '__main__':
    main()