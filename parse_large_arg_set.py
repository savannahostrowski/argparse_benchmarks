import argparse

parser = argparse.ArgumentParser()
for i in range(10000):
    parser.add_argument(f'--arg{i}', type=int)
parser.parse_args([f'--arg{i}' for i in range(10000)])