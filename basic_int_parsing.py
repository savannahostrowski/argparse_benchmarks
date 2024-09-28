import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--num', type=int)
parser.parse_args(['--num', '42'])
