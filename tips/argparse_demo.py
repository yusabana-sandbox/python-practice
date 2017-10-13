import argparse
import sys
from pprint import pprint


def main():
    psr = argparse.ArgumentParser()
    psr.add_argument('-w', '--word', default='hello!')
    psr.add_argument('-s', '--size', default=5, type=int)
    args = psr.parse_args()

    pprint(args.word * args.size)
    pprint(args)


if __name__ == '__main__':
    pprint(sys.version_info)
    main()
