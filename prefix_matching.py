import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo')
parser.parse_args(['--fo', 'bar'])