import sys
import os

print(os.getcwd())
print(os.listdir())

print('*' * 40)


n = sys.stdout.write('abcd') # 改行されない
print(n) # 出力したバイト数

n = sys.stdout.write('abcd\n')
print(n)


print('*' * 40)


x = input('入力x> ')
y = input('入力y> ')
print(int(x) + int(y))

s = sys.stdin.readline()
print(s)

