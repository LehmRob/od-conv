class Node:
    def __init__(self, name, type, id, description, profilename, profile, 
            specificmenu, dictionary, params_dict, ds302, user_mappings):
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
