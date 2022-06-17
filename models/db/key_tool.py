import keyring
import argparse

"""
Tool for storage sensitive data (pass, keys, tokens in security storage
"""

parser = argparse.ArgumentParser(description='Key Access Tool')
parser.add_argument('-KEY_ID', type=str, help='Set Key ID')
parser.add_argument('-KEY', type=str, help='Set Key value')

parser.add_argument('-USER', type=str, help='Set User ID')
parser.add_argument('-PASS', type=str, help='Set Password for User')

parser.add_argument('-GET_KEY', type=str, help='Get Key by KEY ID')
parser.add_argument('-GET_USER', type=str, help='Get password by USER')

parser.add_argument('-STORAGE', type=str, help='Specify storage name')

DEFAULT_STORAGE = 'KEY_ACCESS_TOOL'


def setKeys(name, key, storage=None):
    if storage is None:
        storage = DEFAULT_STORAGE
    try:
        keyring.set_password(storage, name, key)
    except:
        return False
    return True


def readKeys(key, storage=None):
    if storage is None:
        storage = DEFAULT_STORAGE
    return keyring.get_password(storage, key)


def main(args):
    if args.KEY_ID and args.KEY:
        setKeys(args.KEY_ID, args.KEY, args.STORAGE)
    if args.USER and args.PASS:
        setKeys(args.USER, args.PASS, args.STORAGE)
    if args.GET_KEY:
        print(readKeys(args.GET_KEY, args.STORAGE))
    if args.GET_USER:
        print(readKeys(args.GET_USER, args.STORAGE))


if __name__ == '__main__':
    main(parser.parse_args())
