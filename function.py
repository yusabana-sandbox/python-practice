# vim: fileencoding=utf-8

# キーワード引数
def add(a=10, b=20):
    print("a: " + str(a), "b: " + str(b))
    return a + b

# 一部キーワード引数
def add_a_part(a, b=10):
    print("a: " + str(a), "b: " + str(b))
    return a + b

# 可変長引数
def adds(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    return total

# キーワード引数の可変長引数
def keywords(**args):
    result = ''
    for k in args:  # args.items() で key,valueの両方、 args.keys() で keyのみ、args.values() で valueのみ
        result += '{}: {}\n'.format(k, args[k])
    return result

def main():
    print(add())
    print(add(b=2, a=1))
    print(add(a=1))

    print('-' * 30)

    print(adds(1,2,3,4,5))
    print(adds(1,2))

    print('-' * 30)

    print(keywords(a=10))
    print(keywords(a=10, b='spam', ab='ham'))


if __name__ == '__main__':
    main()
