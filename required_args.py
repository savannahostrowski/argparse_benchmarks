import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--age', type=int)
parser.parse_args(['--name', 'Alice'])