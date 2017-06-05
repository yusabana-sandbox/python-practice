# vim: fileencoding=utf-8

def main():
    f = open('spam.txt', 'w', encoding='utf-8')
    f.write('スパム、ハム')
    f.close()

    read_file = open('spam.txt', encoding='utf-8')
    print(read_file.read())
    read_file.close

    # withを使うとブロックを終了すると自動で閉じる
    with open('spam.txt', encoding='utf-8') as f:
        data = f.read()
        print(data)

if __name__ == '__main__':
    main()
