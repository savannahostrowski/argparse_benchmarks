import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

foo_parser = subparsers.add_parser('foo')
foo_subparsers = foo_parser.add_subparsers(dest='foo_command')
foo_subparsers.add_parser('start')
foo_subparsers.add_parser('stop')

parser.parse_args(['foo', 'start'])