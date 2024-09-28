import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', action='store_true')
parser.parse_args(['--verbose'])