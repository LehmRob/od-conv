import node
import argparse
import pickle

parser = argparse.ArgumentParser(description='Print object')
parser.add_argument('-f', '--file', action='store', dest='file')

args = parser.parse_args()

with open(args.file, 'rb') as f:
    node = pickle.load(f)
    print(f'{node.Dictionary}')
