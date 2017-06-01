# vim: fileencoding=utf-8

def main():
    for num in range(1, 101):
        if num % 15 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 ==0:
            print('Buzz')
        else:
            print(num)


if __name__ == '__main__':
    main()

