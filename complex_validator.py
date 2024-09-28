import argparse
def validate_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("Must be a positive integer")
    return ivalue

parser = argparse.ArgumentParser()
parser.add_argument('--positive', type=validate_positive)
parser.parse_args(['--positive', '10'])