import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_const', const=42)
parser.parse_args(['--foo'])