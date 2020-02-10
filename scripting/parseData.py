import sys
import handler
import cleaner

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("USAGE:")
        print(sys.argv[0] + " file1.json [file2.json...]")
        sys.exit(84)
    questions = handler.getListQuestions(sys.argv[1:], cleaner.fullClean)
    questions = list(dict.fromkeys(questions))
    questions = sorted(questions, key=str.casefold)
    for question in questions:
        print(question)
    sys.exit(0)
