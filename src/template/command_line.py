from argparse import ArgumentParser

import template


def main(args=None):
    parser = ArgumentParser(description="Add two values")

    parser.add_argument(
        "-a", dest="a", type=float, required=True, help="The first value"
    )

    parser.add_argument(
        "-b", dest="b", type=float, required=True, help="The second value"
    )

    args = parser.parse_args(args)

    print(template.example(args.a, args.b))
