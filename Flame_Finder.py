def main():
    name1 = "Pranay"
    name2 = "Harika"
    print(word_extractor(name1, name2))


def word_extractor(name1, name2):
    word = set(name1 + name2)
    print("running")
    return word


main()
