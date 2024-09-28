import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--debug', type=bool, choices=[True, False])
parser.parse_args(['--debug', 'True'])