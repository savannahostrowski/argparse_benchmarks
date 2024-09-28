import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str) 
parser.parse_args(['--name', 'Alice'])