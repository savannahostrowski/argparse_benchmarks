import argparse
class CustomFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        return f'*** {action.dest} ***'

def custom_formatter():
    parser = argparse.ArgumentParser(formatter_class=CustomFormatter)
    parser.add_argument('--name', type=str, help="Your name")
    parser.print_help()