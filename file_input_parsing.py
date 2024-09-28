import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=argparse.FileType('r'))
with open('test.txt', 'w') as f:
    f.write('dummy data')
parser.parse_args(['--file', 'test.txt'])
