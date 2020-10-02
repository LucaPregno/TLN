from collections import Counter
from DiCaro.Exercise1.main import main as exercise1
from DiCaro.Exercise2.main import main as exercise2
from DiCaro.Utility.utility import remove


def main():
    print("You can choose between the following exercise:")
    # print("1 Concept similarity")
    # print("2 Content to form")
    # print("3 ")
    # x = int(input("Select the number of the exercise you wanna launch\n"))
    x = 2
    if x == 1:
        print("Concept similarity")
        exercise1()
    elif x == 2:
        print("Content to form")
        exercise2()
    elif x == 3:
        print("")
        exercise2()

    print("\n")


if __name__ == '__main__':
    main()