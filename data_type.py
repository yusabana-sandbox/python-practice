# vim: fileencoding=utf-8


def main():
    print('## LIST ##')
    lis = ['ee', 'aa', 'bb', 'cc', 'dd', 'ee']
    print(lis)
    lis.append('1a')
    print(lis)
    print(lis[1:3])
    print('cc' in lis)
    print('ff' not in lis)
    print(lis.count('ee'))

    lis.sort()
    print(lis)
    lis.reverse()
    print(lis)

    print('-' * 30)


    # タプルは要素の追加や削除ができない
    print('## TUPLE ##')
    tuple = ('AA', 'BB', 'CC')
    print(tuple)
    print('CC' in tuple)

    print('-' * 30)


    print('## DICTIONARY ##')
    dic = dict()
    print(dic)
    dic = { 'spam': 'aaaaa', 'ham': 500 }
    print(dic)
    print(len(dic))
    print('ham' in dic)
    print('ham2' not in dic)

    print(dic.keys())
    print(list(dic.keys()))
    print(list(dic.values()))

    aaa_dict = dict(a=2, b='BBBBB')
    print(aaa_dict)

    print('-' * 30)


    print('## SET ##')
    set_sample = { 'aa', 'bb', 'cc', 'aa' }
    print(set_sample)
    print('aa' in set_sample)

    empty_set = set() # 空のsetは set() で初期化する {} だとDictionaryと判別つかないため
    print(empty_set)
    empty_set.add(2)
    empty_set.add(1)
    empty_set.add(1)
    empty_set.discard(2)
    print(empty_set)
    empty_set.clear()
    print(empty_set)

    frozened = frozenset(set_sample)
    print('aa' in frozened)
    print('a' not in frozened)

if __name__ == '__main__':
    main()
