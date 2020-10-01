from collections import Counter
from DiCaro.Exercise1.main import main as exercise1
from DiCaro.Exercise2.main import main as exercise2
from DiCaro.Utility.utility import remove


def main():
    print("You can choose between the following exercise:")
    # print("1 Concept similarity")
    # print("2 Content to form")
    # x = int(input("Select the number of the exercise you wanna launch\n"))
    x = 2
    if x == 1:
        print("Concept similarity")
        exercise1()
    elif x == 2:
        print("Content to form")
        exercise2()

    # counterA = Counter(['apple', 'banana', 'banana', 'coconut', 'ever', 'ever'])
    # counterB = Counter(['apple', 'apple', 'banana', 'banana', 'coconut', 'dinner'])
    # print("somma", counterA + counterB)
    # print("&", counterA & counterB)
    # print("sottrazione", counterA - counterB)
    # print(counterA.update(counterB))
    # print(counterA)
    # dct = {1: '1', 2 : '2'}
    # prova = dict(filter(lambda x: x[1] >= 2, counterA.items()))
    #
    # # x = list(filter(lambda c : c[1] > 1, counterA.__iter__()))
    # print("Stampa X", x)
    # print("Stampa DCT", prova)

    print("\n")


if __name__ == '__main__':
    main()