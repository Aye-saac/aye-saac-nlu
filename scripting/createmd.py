import sys
import os

def mergeFiles(directory: str, outputFile):
    '''
    Puts a / at the end of the directory string for further concatenation
    List all file and sub directories in the given directory:
        If it is a file and the file ends with the .md extension:
            reads its content and writes it in the given output file
        If it is a directory:
            recursively calls this function
        Otherwise just pass
    '''
    if not directory.endswith("/"):
        directory += "/"
    listdir = os.listdir(directory)
    # print("dir => " + directory)
    # print(listdir)
    for it in listdir:
        fullpath = directory + it
        if os.path.isfile(fullpath) and fullpath.endswith(".md"):
            try:
                with open(fullpath, 'r') as file:
                    for line in file.readlines():
                        outputFile.write(line)
                        if not line.endswith("\n"):
                            outputFile.write("\n")
                outputFile.write("\n")
            except IOError as e:
                print(e)
        elif os.path.isdir(fullpath):
            mergeFiles(fullpath, outputFile)

def mergeContents(lines: list, indexFirst: int, indexSecond: int):
    '''
    Merges the content of 2 parts into the first one given their indexes
    Deletes all unnecessary lines
    '''
    # print("first => " + str(indexFirst))
    # print("second => " + str(indexSecond))
    lines.pop(indexSecond)
    while len(lines[indexSecond].strip()) != 0:
        lines.insert(indexFirst + 1, lines.pop(indexSecond))
        indexSecond += 1
    try:
        while len(lines[indexSecond].strip()) == 0:
            lines.pop(indexSecond)
    except IndexError:
        pass

def mergeContentsHandler(output: str):
    '''
    Reads the content of the given output file
    Go through all the lines to find a specific part
    Once a part has been found:
        Looks if the same part occurs anywhere else on the file
        If so calls the mergeContents function to merge contents
        Otherwise just pass
    '''
    try:
        with open(output, 'r') as file:
            lines = file.readlines()
            try:
                for i in range(0, len(lines)):
                    line = lines[i]
                    if line.startswith("## intent:") or line.startswith("## synonym:") or line.startswith("## lookup:") or line.startswith("## regex:"):
                        try:
                            index = lines[(i+1):].index(line) + (i + 1)
                            mergeContents(lines, i, index)
                        except ValueError:
                            pass
                    # print("i => " + str(i) + " = " + lines[i].strip())
            except IndexError:
                pass
            finally:
                try:
                    with open(output, 'w') as file:
                        for line in lines:
                            file.write(line)
                except IOError as e:
                    print(e)
    except IOError as e:
        print(e)

def handler(directory: str, output: str):
    '''
    Makes some verifications on given parameters and prints error messages if necessary
    Calls the different functions of the program
    '''
    clean = True
    if not os.path.isdir(directory):
        print("Directory: '" + directory + "' doesn't exist or isn't a directory. Please verify given name.")
        clean = False
    if not output.endswith(".md"):
        print("Output: '" + output + "' doesn't have the .md extension. Please verify given name.")
        clean = False
    if clean == True:
        try:
            with open(output, 'w') as file:
                mergeFiles(directory, file)
            mergeContentsHandler(output)
        except IOError as e:
            print(e)

if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print("USAGE:")
        print(sys.argv[0] + " directory output.md")
        print("")
        print("DESCRIPTION:")
        print("Reads recursively all .md files starting from given directory, merges them and writes the result into given output.md file.")
        sys.exit(84)
    directory = sys.argv[1]
    output = sys.argv[2]
    handler(directory, output)
