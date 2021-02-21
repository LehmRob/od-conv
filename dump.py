import node
import argparse
import pickle

def print_dict(data):
    for index, values in data.items():
        print(f'    --{hex(index)}')
        if type(values) == list:
            for val in values:
                print(f'      > {val}')
        else:
            print(f'      > {values}')

parser = argparse.ArgumentParser(description='Print object')
parser.add_argument('-f', '--file', action='store', dest='file')

args = parser.parse_args()

node = node.Node()

node.load_from_file(args.file)

# with open(args.file, 'rb') as f:
    # node = pickle.load(f)

print(f'OD File for {node.Name}')
print(f'  Type:          {node.Type}')
print(f'  ID:            {node.ID}')
print(f'  Description:   {node.Description}')
print(f'  Profile Name:  {node.ProfileName}')
print(f'  Profile:       {node.Profile}')
print(f'  Dictionary:')

print_dict(node.Dictionary)

print(f'  ParamsDictionary:')

print_dict(node.ParamsDictionary)

print(f'  Usermappings:')

print_dict(node.UserMapping)
