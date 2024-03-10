import argparse
import glob
import fileinput
import logging

from . import wilt


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)-7s %(name)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    parser = argparse.ArgumentParser()
    parser.add_argument('glob', help='file, glob or -')
    parser.add_argument('-i', help='indentation size', dest='indent', type=int, default=4)
    args = parser.parse_args()

    files = args.glob
    if args.glob != '-':
        files = glob.glob(files, recursive=True)
        if not files:
            parser.error('No files found')

    with fileinput.input(files) as fp:
        print(wilt.wilt(fp, indent=args.indent))
