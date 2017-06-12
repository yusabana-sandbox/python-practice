# -*- coding: utf-8 -*-

try:
    f = open('hoge.txt')
    num - int(f.read())
    print('数値は {} です'.format(num))
except OSError as err:
    print('ファイルが開けませんでした: {}'.format(err))
except ValueError as err:
    print('数値への変換に失敗しました: {}'.format(err))
