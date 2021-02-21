#!/usr/bin/env python

import argparse
import gnosis

parser = argparse.ArgumentParser(description='Convert gnosis to native pickle')

parser.add_argument('-i', '--input', action='store', dest='inputFile')
parser.add_argument('-o', '--output', action='store', dest='outputFile')

args = parser.parse_args()

with open(args.inputFile, 'r') as f:
	node = gnosis.xml.pickle.load(f)

print node