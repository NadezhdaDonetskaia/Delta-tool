import argparse
import json


parser = argparse.ArgumentParser(description='Generate diff', prog='gendiff')
parser.add_argument('first_file', metavar='first_file',
                    help='path to first_file')
parser.add_argument('second_file', metavar='second_file',
                    help='path to second_file')
parser.add_argument('-f', '--format', dest='FORMAT',
                    help='set format of output')

args = parser.parse_args()


def generate_diff(first_file, second_file) -> str:
    first_file = json.load(open(first_file))
    second_file = json.load(open(second_file))
    accum_keys = first_file.copy()
    accum_keys.update(second_file)
    accum_keys = [el for el in accum_keys]
    accum_keys.sort()
    result = '{\n'
    for key in accum_keys:
        if key in first_file and key in second_file:
            if first_file[key] != second_file[key]:
                result += f'    - {key}: {first_file[key]}\n    ' \
                          f'+ {key}: {second_file[key]}\n'
            else:
                result += f'      {key}: {first_file[key]}\n'
        elif key in first_file:
            result += f'    - {key}: {first_file[key]}\n'
        else:
            result += f'    + {key}: {second_file[key]}\n'
    result += '}'
    return result


def main():
    if args.first_file and args.second_file:
        print(generate_diff(args.first_file, args.second_file))
    # else:
    #     print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
