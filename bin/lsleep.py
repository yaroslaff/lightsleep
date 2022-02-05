#!/usr/bin/python3

import argparse
from lightsleep import Sleep

def get_args():
    parser = argparse.ArgumentParser(description='Sleep which can awake')
    parser.add_argument('seconds', type=int)
    parser.add_argument('--hook', nargs='+', metavar=('METHOD', 'ARG'))
    return parser.parse_args()

def main():
    args = get_args()

    s = Sleep(hook=args.hook)
    s.sleep(args.seconds)

if __name__ == '__main__':
    main()