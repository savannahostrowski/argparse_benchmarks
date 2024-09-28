import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--num', type=int, default=10)
parser.add_argument('--flag', action='store_true')
parser.parse_args([])