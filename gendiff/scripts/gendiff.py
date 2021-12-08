#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


parser = argparse.ArgumentParser(description='Generate diff', prog='gendiff',
                                 # usage='%(prog)s -f stylish'
                                 )
parser.add_argument('first_file', metavar='first_file',
                    help='path to first_file')
parser.add_argument('second_file', metavar='second_file',
                    help='path to second_file')
parser.add_argument('-f', '--format', dest='FORMAT', default='stylish',
                    help='set format of output')

args = parser.parse_args()


def main():
    print(args)
    if args.first_file and args.second_file:
        print(generate_diff(args.first_file, args.second_file, args.FORMAT))
    # else:
    #     print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
