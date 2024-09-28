import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str)
parser.add_argument('--age', type=int)
parser.parse_args(['--name', 'Alice', '--age', '30'])