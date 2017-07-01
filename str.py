# vim: fileencoding=utf-8

a = """bbbbbb
aaaaaaaaaa
"""

b = '''aaaaa
dfdfd3'''


print(a)
print('--------------')
print(b)


print('=================')

print(str(1))
print(int('1'))

print('=================')

print('3' in b)

print('=================')

m1 = 'I am {}'.format('Yujiii')
print(m1)

m2 = '{2}-{2} {0} {1}'.format('aa', 'bb', 'cc')
print(m2)

m3 = '{aa} AND {bb}'.format(bb='なんだって', aa=1)
print(m3)

m4 = '|{2:7s}|{1:7s}|{0:7s}|'.format('aaa', 'bbbccccccccccZ', 'cccbbb')
print(m4)

m5 = '|{2:7.2f}|{1:7.2f}|{0:7.3f}|'.format(1.2, 3.3, 5.5)
print(m5)


print('=================')

aa = ['1', '2', 'bb']
print(','.join(aa))

print('=================')

name = 'Yuji'
m6 = 'あいうえお %s' % name
print(m6)

# リストやタプルを文字列展開する場合
print('list is %s' % ['aaaa', 1, 2])
# http://qiita.com/tomotaka_ito/items/594ee1396cf982ba9887
print('divmod: %s' % (divmod(5, 2),))

print('aaa is %(a)s' % dict(a='AAA'))

print('|%7s|%7s|%7s|' % ('one', 'two', 'three'))
print('|%7d|%7d|%7d|' % (1, 2, 3))
print('|%7.2f|%7.2f|%7.4f|' % (1.1, 2.22, 3.333))
print('|%-7s|%-7s|%-7s|' % ('one', 'two', 'three'))


print('=================')

str = 'abcdefghijklmnopqrstuvwxyz'
print(len(str))
print(str[:23])
print(str[0:])
print(str[:])
print(str[::2])  # 添字が偶数番目の取り出し(先頭から一つ飛ばし)
print(str[1::2]) # 添字書き数番目の取り出し
print(str[::-1]) # 逆順取り出し

print('=================')

# バイト列の変換
str = '日本語'
str_enc = str.encode('utf-8')
str_dec = str_enc.decode('utf-8')
print(str)
print(str_enc)
print(str_dec)
