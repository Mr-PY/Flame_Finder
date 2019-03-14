def main():
    person1 = input("Enter the First Person's name: ").replace(' ', '')
    person2 = input("Enter the second Person's name: ").replace(' ', '')
    print(count_letters(person1, person2))
    print(person1, person2)
# Extracting Words from names ###


def count_letters(person1, person2):
    common_characters = list(set(person1).intersection(set(person2)))
    for character in common_characters:
        person1 = person1.replace(character, '')
        person2 = person2.replace(character, '')
    word_length = len(person1 + person2)
    return word_length

# TODO: flames logic and printing the flame character
main()
