import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
parser.add_argument('output_file', type=str)
parser.parse_args(['input.txt', 'output.txt'])