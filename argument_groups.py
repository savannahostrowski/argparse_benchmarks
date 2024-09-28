import argparse

parser = argparse.ArgumentParser()
group1 = parser.add_argument_group('group1')
group1.add_argument('--foo', type=int)
group2 = parser.add_argument_group('group2')
group2.add_argument('--bar', type=str)
parser.parse_args(['--foo', '10', '--bar', 'hello'])