# -*- coding: utf-8 -*-
# Pythonの内包表記の使い方まとめ - Life with Python
#   http://www.lifewithpython.com/2014/09/python-list-comprehension-and-generator-expression-and-dict-comprehension.html

def main():
    ## リスト内包
    list = [number + 1 for number in range(1,5)]
    print(list)

    print([x * y for x, y in zip([1,2,3], [11,12,13])])
    # 条件(値部分で条件を入れる)
    print(['タァーん' if x % 3 == 0 else x for x in range(1,10)])
    print([('fizzbuzz' if x % 15 == 0 else ('fizz' if x % 3 == 0 else ('buzz' if x % 5 == 0 else x))) for x in range(1, 30)])
    # 条件(後置ifで条件を入れる)
    print(['タァーん %d' % x for x in range(1,10) if x % 3 == 0 ])
    # 多重ループ
    print([x + y for x in range(3) for y in [100, 200, 300]])
    # ネスト(flattenな配列にする)
    print([x for inner_list in [[1, 3], [5], [7, 9]] for x in inner_list])


    ## ジェネレータ内包(Rubyのイテレータのような)
    generator = (x + 1 for x in range(5))
    for x in generator:
        print(x)

    ## Set(集合)内包
    set = {x for x in range(5) if x % 2 == 0}
    print(set)

    ## ディクショナリ(辞書)
    words = 'あいうえおあ'
    dict = {letter: words.count(letter) for letter in words}
    print(dict)

    li = [("C", 1972), ("Java", 1995), ("JavaScript", 1995)]
    print({k: v for k, v in li})

if __name__ == '__main__':
    main()
