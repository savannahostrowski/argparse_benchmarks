import argparse
import os

os.environ['NAME'] = 'Alice'
parser = argparse.ArgumentParser()
parser.add_argument('--name', default=os.getenv('NAME'))
parser.parse_args([])
