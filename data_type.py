# vim: fileencoding=utf-8


def main():
    print('## LIST ##')
    list = ['aa', 'bb', 'cc', 'dd', 'ee']
    print(list)
    list.append(1)
    print(list)
    print(list[1:3])
    print('cc' in list)

    print('-' * 30)

    # タプルは要素の追加や削除ができない
    print('## TUPLE ##')
    tuple = ('AA', 'BB', 'CC')
    print(tuple)
    print('CC' in tuple)

    print('-' * 30)

    print('## DICTIONARY ##')
    dict = { 'spam': 'aaaaa', 'ham': 500 }
    print(dict)
    print(len(dict))
    print('ham' in dict)

    print('-' * 30)

    print('## SET ##')
    set = { 'aa', 'bb', 'cc', 'aa' }
    print(set)
    print('aa' in set)


if __name__ == '__main__':
    main()
