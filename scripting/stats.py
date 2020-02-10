import sys
import handler
import cleaner
import pandas as pd

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("USAGE:")
        print(sys.argv[0] + " file1.json [file2.json...]")
        sys.exit(84)
    questions = handler.getListQuestions(sys.argv[1:], cleaner.softClean)
    histogram = pd.Series(questions).value_counts()

    # print(histogram)
    print("-------------- BEST30 --------------")
    print(histogram[:30])
    sys.exit(0)
