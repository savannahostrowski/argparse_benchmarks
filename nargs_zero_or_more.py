import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--items', nargs='*', type=str)
parser.parse_args(['--items', 'apple', 'banana', 'orange'])
