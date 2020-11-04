from DiCaro.Exercise1.main import main as exercise1
from DiCaro.Exercise2.main import main as exercise2
from DiCaro.Exercise3.main import main as exercise3
from DiCaro.Exercise4.main import main as exercise4
from DiCaro.Utility.utility import remove


def main():
    print("You can choose between the following exercise:")
    # print("1 Concept similarity")
    # print("2 Content to form")
    # print("3 Hanks")
    # print("4 Document segmentation")
    # x = int(input("Select the number of the exercise you wanna launch\n"))
    x = 4
    if x == 1:
        print("Concept similarity")
        exercise1()
    elif x == 2:
        print("Content to form")
        exercise2()
    elif x == 3:
        print("Hanks")
        words = []
        word = ""
        while "ok" != word:
            print("Type: ok if you want to start the program")
            word = input("Type verb\n")
            words.append(word)
        exercise3(words)
    elif x == 4:
        print("Document segmentation")
        exercise4()

    print("\n")


if __name__ == '__main__':
    main()
