import json
import cleaner

def fillArray(array, filename, key, cleanerfct):
    '''Fills an array with the data coming from a given json file'''

    # Open file and read from json file to fill the array
    try:
        with open(filename) as file:
            data = json.load(file)
            for line in data:
                array.append(cleanerfct(line[key]))
    except IOError:
        print("File: '" + filename + "' not accessible. Permission denied.")
