#!/usr/bin/env python

import argparse
import gnosis.xml.pickle
import pickle as pic
import node

parser = argparse.ArgumentParser(description='Convert gnosis to native pickle')

parser.add_argument('-i', '--input', action='store', dest='inputFile')
parser.add_argument('-o', '--output', action='store', dest='outputFile')

args = parser.parse_args()

with open(args.inputFile, 'r') as f:
    print "Loading gnosis file {}".format(args.inputFile)
    old_node = gnosis.xml.pickle.load(f)
    print old_node.Name
    new_node = node.Node(old_node.Name, old_node.Type, old_node.ID, 
            old_node.Description, old_node.ProfileName, old_node.Profile, 
            old_node.SpecificMenu, old_node.Dictionary, 
            old_node.ParamsDictionary, old_node.DS302, old_node.UserMapping)

with open(args.outputFile, 'wb') as f:
    print "Storing the data to {}".format(args.outputFile)
    pic.dump(new_node, f, protocol=pic.HIGHEST_PROTOCOL)
