#! /usr/bin/env python

import argparse
from open_site import open_site


def run(args):
    open_site(args.input, args.openBrowser)


def main():
    parser = argparse.ArgumentParser(
        description="This interface can be used to search through the nature research journal for articles of interest"
    )

    parser.add_argument(
        "--input",
        nargs="+",
        help="This argument excepts the url to nature journal search bar and then the desired search term.",
        dest="input",
        type=str,
        required=True,
    )

    parser.add_argument(
        "--openBrowser",
        help="This argument excepts True or False and if True will open the web page",
        dest="openBrowser",
        type=bool,
        required=False,
        default=False,
    )

    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

