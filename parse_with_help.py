import argparse
parser = argparse.ArgumentParser(description="Benchmark argparse help generation")
parser.add_argument('--foo', type=int, help="The foo argument")
parser.add_argument('--bar', type=str, help="The bar argument")
parser.print_help()