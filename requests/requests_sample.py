# -*- coding: utf-8 -*-
import requests


def main():
    r = requests.get('http://google.com')
    print(r.text[:100])


if __name__ == '__main__':
    main()
