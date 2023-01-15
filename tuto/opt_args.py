import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output', action='store_true', help='show output')
parser.add_argument('-n','--name', dest='names', action='append', help='provides names to greet')

args = parser.parse_args()


if args.output:
    print("this is some output")

names = args.names
for name in names:
    print(f'Hello {name}!')



