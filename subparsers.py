import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

foo_parser = subparsers.add_parser('foo')
foo_parser.add_argument('--foo-arg', type=int)

bar_parser = subparsers.add_parser('bar')
bar_parser.add_argument('--bar-arg', type=str)

parser.parse_args(['foo', '--foo-arg', '42'])