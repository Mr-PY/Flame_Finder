def starting_point():
    person1 = input("Enter the First Person's name: ")
    name1 = person1.replace(' ', '')
    person2 = input("Enter the second Person's name: ")
    name2 = person2.replace(' ', '')
    word_count = count_letters(name1.lower(), name2.lower())
    if name1.isalpha() and name2.isalpha():
        flame_character = finding_flame(word_count)
        flame_definer(person1, person2, flame_character)
    else:
        print("Please enter valid names")


# ---Extracting Unique letters as a word from names---
def count_letters(name1, name2):
    common_characters = list(set(name1).intersection(set(name2)))
    for character in common_characters:
        name1 = name1.replace(character, '')
        name2 = name2.replace(character, '')
    word_length = len(name1 + name2)
    return word_length


# ---Flames Logic---
def finding_flame(word_length):
    flame_word = 'FLAME'
    flame_value = word_length % 5
    return flame_word[flame_value - 1]


# ---flame output/final output---
def flame_definer(name1, name2, flame_character):
    if flame_character == 'F':
        print(f"{name1} and {name2} are destined to be Friends")
    elif flame_character == 'L':
        print(f"{name1} and {name2} are destined to be Lovers")
    elif flame_character == 'A':
        print(f"{name1} and {name2} are destined to be Affectionate")
    elif flame_character == 'M':
        print(f"{name1} and {name2} are destined to be Married")
    elif flame_character == 'E':
        print(f"{name1} and {name2} are destined to be Enemies")


starting_point()
