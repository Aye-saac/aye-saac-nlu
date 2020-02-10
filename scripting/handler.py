import fileReader
import os

def getListQuestions(files, cleanerfct):
    '''Returns the list of questions from given files'''

    # Get the questions as an array
    questions = []
    for file in files:
        if (os.path.isfile(file)):
            fileReader.fillArray(questions, file, 'question', cleanerfct)
        else:
            print("File: '" + file + "' doesn't exist or isn't a file. Verify given filename.")
    return questions
