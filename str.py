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

m2 = '{2} {0} {1}'.format('aa', 'bb', 'cc')
print(m2)

m3 = '{aa} AND {bb}'.format(bb='なんだって', aa=1)
print(m3)


name = 'Yuji'
m4 = 'あいうえお %s' % name
print(m4)

print('=' * 20)
aa = ['1', '2', 'bb']
print(','.join(aa))
# リストやタプルを文字列展開する場合
print('list is %s' % ['aaaa', 1, 2])
# http://qiita.com/tomotaka_ito/items/594ee1396cf982ba9887
print('divmod: %s' % (divmod(5, 2),))


print('aaa is %(a)s' % dict(a='AAA'))


str = 'abcdefghijklmnopqrstuvwxyz'
print(len(str))
print(str[:23])
print(str[0:])
print(str[:])
print(str[::2])  # 添字が偶数番目の取り出し(先頭から一つ飛ばし)
print(str[1::2]) # 添字書き数番目の取り出し
print(str[::-1]) # 逆順取り出し
