import pickle

class Node:
    def __init__(self, name = "", type = "", id = 0, description = "", profilename = "", 
            profile="", specificmenu = None, dictionary = None, params_dict = None, 
            ds302 = None, user_mappings = None):
        self.Name = name
        self.Type = type
        self.ID = id
        self.Description = description
        self.ProfileName = profilename
        self.Profile = profile
        self.SpecificMenu = specificmenu
        self.Dictionary = dictionary
        self.ParamsDictionary = params_dict
        self.DS302 = ds302
        self.UserMapping = user_mappings

    def load_from_file(self, filename):
        with open(filename, 'rb') as f:
            data = pickle.load(f)

        self.Name = data.Name
        self.Type = data.Type
        self.Type = data.Type
        self.ID = data.ID
        self.Description = data.Description
        self.ProfileName = data.ProfileName
        self.Profile = data.Profile
        self.SpecificMenu = data.SpecificMenu
        self.Dictionary = data.Dictionary
        self.ParamsDictionary = data.ParamsDictionary
        self.DS302 = data.DS302
        self.UserMapping = data.UserMapping


class ObjectEntry:
    def __init__(self, name:str, od_type:int, access:str):
        self.name = name
        self.od_type = od_type,
        self.access = access
