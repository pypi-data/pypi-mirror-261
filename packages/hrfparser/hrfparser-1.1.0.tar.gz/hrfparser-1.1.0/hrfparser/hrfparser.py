'''Copyright (c) 2024 Sean Yeatts. All rights reserved.'''


# IMPORTS - EXTERNAL
import yaml                         # yaml
import json                         # json
from quickpathstr import Filepath   # file syntax reducer


# CLASSES
class FlowStyle(yaml.SafeDumper):
    '''
    Custom formatting of lists ( sequences ) to enforce inline representation.
    '''
    def represent_sequence(self, tag, sequence, flow_style=None):
        # Force flow style for lists (sequences)
        return super(FlowStyle, self).represent_sequence(tag, sequence, flow_style=True)

# Let PyYAML know about our custom formatter
yaml.add_representer(list, FlowStyle.represent_list, Dumper=FlowStyle)


# FORMATTED METHODS : deconstruct / rebuild policy
def unpack(file: Filepath) -> dict:
    '''
    Reads HRF and flattens into single key-value pairs.

    Params:
        - file ( Filepath ) : source file
    '''
    data = read(file)
    return flatten(data)

def pack(data: dict, file: Filepath):
    '''
    Rebuilds single key-value pairs and writes to HRF.
    
    Params:
        - data ( dict ) : dictionary
        - file ( Filepath ) : destination file
    '''
    data = fold(data)
    write(data, file)

# UNFORMATTED METHODS : use 'as-is' policy
def read(file: Filepath) -> dict:
    '''
    Reads HRF into Python dictionary.
                    
    Params:
        - file ( Filepath ) : source file
    '''

    # Access source file
    try:
        source = open(file.complete, 'r')
    except Exception as error:
        print(f"File access issue: {str(error)}")
    
    # Select appropriate read method based on file extension
    match file.extension:
        case '.yaml':
            return yaml.safe_load(source)
        case '.json':
            return json.load(source)
        case _:
            raise KeyError(f"File extension '{file.extension}' not supported!")

def write(data: dict, file: Filepath):
    '''
    Writes Python dictionary to HRF.
            
    Params:
        - data ( dict ) : dictionary
        - file ( Filepath ) : destination file
    '''
    
    # Access destination file
    try:
        destination = open(file.complete, 'w')
    except Exception as error:
        print(f"File access issue: {str(error)}")
    
    # Select appropriate write method
    match file.extension:
        case '.yaml':
            # Not safedump(), but uses a safedump-derived dumper
            yaml.dump(data, destination, sort_keys=False, Dumper=FlowStyle)
        case '.json':
            json.dump(data, destination, sort_keys=False, indent=2)
        case _:
            raise KeyError(f"File extension '{file.extension}' not supported!")

# FORMATTING TOOLS
def flatten(data: dict) -> dict:
    '''
    Flattens nested dicts into single key-value pairs.
    
    Params:
        - data ( dict ) : nested dictionary

    Returns:
        - ( dict ) : flattened dictionary ( keys are tuples )
    '''
    result = {}

    # Recursive traversal of nested structures
    def traverse(source, old_key=[]):

        # Iterate on each key-value pair
        for key, value in source.items():   # for each item
            new_key = old_key + [key]       # update current key path

            # Check the nature of the value
            if isinstance(value, dict):             # if we're still seeing a dictionary...
                nesting = traverse(value, new_key)  # go one deeper
                result.update(nesting)              # when we get back out, overwrite entry
            else:
                result[tuple(new_key)] = value      # ...otherwise create entry
        return result
    return traverse(data)

def fold(data: dict) -> dict:
    '''
    Rebuilds a nested dict from single key-value pairs.
            
    Params:
        - data ( dict ) : flat dictionary

    Returns:
        - ( dict ) : folded dictionary ( keys are tuples )
    '''
    result = {}
    
    def set_value(d, keys, value):
        if isinstance(keys, tuple):
            for key in keys[:-1]:  # all keys except the last one
                d = d.setdefault(key, {})
            d[keys[-1]] = value
        else:
            d[keys] = value

    for keys, value in data.items():
        if isinstance(value, dict):
            nested_dict = fold(value)
            set_value(result, keys, nested_dict)
        else:
            set_value(result, keys, value)

    return result
