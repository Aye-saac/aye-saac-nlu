from string import punctuation

def commonClean(line):
    '''Common line cleaner for all purposes'''

    # Copy
    cleanedLine = line
    # Make lowercase
    cleanedLine = cleanedLine.lower()
    # Remove trailing spaces and punctuation
    savedLine = None
    while savedLine != cleanedLine:
        savedLine = cleanedLine
        cleanedLine = cleanedLine.strip()
        cleanedLine = cleanedLine.strip(punctuation)

    return cleanedLine

def fullClean(line):
    '''Fully cleans a line and returns it'''

    cleanedLine = commonClean(line)

    # Remove 'thank you', 'please', 'can you', duplicated spaces
    # Remove space in front of commas and remove duplicated commas
    savedLine = None
    while savedLine != cleanedLine:
        savedLine = cleanedLine
        cleanedLine = cleanedLine.replace('thank you', '')
        cleanedLine = cleanedLine.replace('please', '')
        cleanedLine = cleanedLine.replace('can you', '')
        cleanedLine = cleanedLine.replace('what\'s in', 'what is in')
        cleanedLine = cleanedLine.replace('what\'s on', 'what is on')

        cleanedLine = cleanedLine.strip()
        cleanedLine = cleanedLine.strip(punctuation)
        cleanedLine = cleanedLine.replace('  ', ' ')
        cleanedLine = cleanedLine.replace(' ,', ',')
        cleanedLine = cleanedLine.replace(',,', ',')
        if len(cleanedLine) == 0:
            cleanedLine = savedLine

    return cleanedLine

def softClean(line):
    '''Softly cleans a line and returns it (for stats purpose only)'''

    cleanedLine = commonClean(line)
    return cleanedLine
