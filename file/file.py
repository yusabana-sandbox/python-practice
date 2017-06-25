# vim: fileencoding=utf-8

def main():
    f = open('spam.txt', 'w', encoding='utf-8')
    f.write('スパム、ハム\n')
    f.write('hoge,fuga')
    f.close()

    read_file = open('spam.txt', encoding='utf-8')
    print(read_file.read())
    read_file.close

    print('*' * 30)

    read_file2 = open('spam.txt', encoding='utf-8')
    while True:
        s = read_file2.readline().rstrip() # readlineが改行コードも含めて取得するので余計な改行コードが含まれる
        if s:
            print(s)
        else:
            break

    print('*' * 30)

    # withを使うとブロックを終了すると自動で閉じる
    with open('spam.txt', encoding='utf-8') as f:
        data = f.read()
        print(data)

if __name__ == '__main__':
    main()
