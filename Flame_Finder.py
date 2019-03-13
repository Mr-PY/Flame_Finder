def main():
    name1 = input("Enter the First Person's name ").replace(' ', '')
    name2 = input("Enter the second Person's name ").replace(' ', '')
    print(word_extractor(name1, name2))


def word_extractor(name1, name2):
    word = set(name1 + name2)
    print("running")
    return word


main()
