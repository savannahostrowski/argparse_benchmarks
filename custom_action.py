import argparse

class CustomAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values.upper())


parser = argparse.ArgumentParser()
parser.add_argument('--name', action=CustomAction)
parser.parse_args(['--name', 'alice'])