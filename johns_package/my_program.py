import sys
import argparse


def create_parser():
    """Return argument parser for pbrain training interface."""
    p = argparse.ArgumentParser()

    p.add_argument(
        '--name',
        required=False,
        default=None
        help="Provide your name."
        )


def parse_args(args):
    """Return namespace of arguments."""
    parser = create_parser()
    parsed_args = parser.parse_args(args)
    return parsed_args


def main(args=None):
    if args is None:
        parsed_args = parse_args(sys.argv[1:])
        if parsed_args.name:
            print(f"Hello {args.name}")
        else:
            print("Hello. Hmmm... have we met? I don't know your name")


if __name__ == '__main__':
    main()