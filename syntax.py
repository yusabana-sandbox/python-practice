# vim: fileencoding=utf-8


def main():
    print('## for ##')
    list = ['aa', 'bb', 'cc']
    for data in list:
        print(data)

    for i in range(10):
        print(i)

    for i, data in enumerate(list):
        print(i, data)


if __name__ == '__main__':
    main()
