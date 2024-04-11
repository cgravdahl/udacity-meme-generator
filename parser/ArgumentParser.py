import argparse
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.resolve()
DATA_ROOT = PROJECT_ROOT / 'data'


def make_parser():
    parser = argparse.ArgumentParser(
        description='Create memes with text!'
    )
    parser.add_argument('-p', '--path', default=None, type=pathlib.Path,
                        help='Path to the image file, if none provided, it will pull a random image')
    parser.add_argument('-b', '--body',default=None,
                        help='Text for the meme')
    parser.add_argument('-a', '--author',default=None, help='Author for the quote')

    return parser
