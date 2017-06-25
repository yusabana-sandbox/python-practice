# vim: fileencoding=utf-8


def main():
    print('## for ##')
    lis = ['aa', 'bb', 'cc']
    for data in lis:
        print('data=', data)

    print('*' * 40)

    for i in range(10):
        print(i)

    print('*' * 40)

    for i in range(1, 10, 2):
        print(i)
    else:
        print('終了')

    print('*' * 40)

    for i, data in enumerate(lis):
        print(i, data)

    print('*' * 40)

    numbers = [ x**2 for x in range(10) ]
    print(numbers)


    print('## while ##')

    n = 0
    while n < 10:
        if n == 2:
            n += 2
            continue

        print(n)
        n += 2
    else:
        print('終了')




if __name__ == '__main__':
    main()
