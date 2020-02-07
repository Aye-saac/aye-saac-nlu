import json
import sys

def cleaner(line):
    '''Cleans a line and returns it'''

    cleanedLine = line
    # Make lowercase
    cleanedLine = cleanedLine.lower()
    # Remove trailing spaces
    cleanedLine = cleanedLine.strip()
    return cleanedLine

def filler(questions, filename):
    '''Fills an array with the data coming from a given json file'''

    # Open file and read from json file to fill the array
    with open(filename) as file:
        data = json.load(file)
        for line in data:
            questions.append(cleaner(line['question']))

def getListQuestions():
    '''Returns the list of questions from dataset'''

    directory = sys.argv[1]

    # Get the questions as an array
    questions = []
    filler(questions, directory + "train.json")
    filler(questions, directory + "test.json")
    filler(questions, directory + "val.json")
    return questions

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("USAGE:")
        print(sys.argv[0] + " dataDirectory")
        sys.exit(84)
    questions = getListQuestions()
    questions = sorted(questions, key=str.casefold)
    questions = list(dict.fromkeys(questions))
    for question in questions:
        print(question)
    sys.exit(0)
