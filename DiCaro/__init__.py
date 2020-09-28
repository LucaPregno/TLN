from DiCaro.Exercise1.main import main as exercise1


def main():
    print("You can choose between the following exercise:")
    print("1 Concept similarity")
    # x = int(input("Select the number of the exercise you wanna launch\n"))
    x = 1
    if x == 1:
        exercise1()

    print("\n")


if __name__ == '__main__':
    main()