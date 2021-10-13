import json


def get_regions(config_file):
    ''' Loads regions from config '''
    
    return json.load(open(config_file))


if __name__ == "__main__":
    print('This is a library.')
