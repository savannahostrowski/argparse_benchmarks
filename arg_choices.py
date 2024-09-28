import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--color', choices=['red', 'green', 'blue'])
parser.parse_args(['--color', 'red'])