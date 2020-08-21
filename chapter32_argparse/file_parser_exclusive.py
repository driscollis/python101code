# file_parser_exclusive.py

import argparse

def file_parser(input_file, output_file=''):
    print(f'Processing {input_file}')
    print('Finished processing')
    if output_file:
        print(f'Creating {output_file}')

def main():
    parser = argparse.ArgumentParser('File parser',
                                     description='PyParse - The File Processor',
                                     epilog='Thank you for choosing PyParse!',
                                     add_help=False)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--infile', help='Input file for conversion')
    group.add_argument('-o', '--out', help='Converted output file')
    args = parser.parse_args()
    if args.infile:
        file_parser(args.infile, args.out)

if __name__ == '__main__':
    main()