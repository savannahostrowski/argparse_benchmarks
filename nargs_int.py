import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--coords', nargs=2, type=int)
parser.parse_args(['--coords', '10', '20'])
