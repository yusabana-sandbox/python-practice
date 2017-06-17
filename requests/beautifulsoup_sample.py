# -*- coding: utf-8 -*-
import requests

from bs4 import BeautifulSoup

def main():
    r = requests.get('http://gihyo.jp/magazine/SD')
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.title)
    print(soup.title.text)

    print('=' * 30)

    outline = soup.find(id='magazineTopOutline')
    for title in outline.find_all(class_='title'):
        print(title.text)


if __name__ == '__main__':
    main()
