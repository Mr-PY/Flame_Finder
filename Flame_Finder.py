def user_input():
    person1 = input("Enter the First Person's name: ").replace(' ', '')
    person2 = input("Enter the second Person's name: ").replace(' ', '')
    word_count = count_letters(person1.lower(), person2.lower())
    # print(word_count)
    # print(finding_flame(word_count))
    # print(person1, person2)
    flame_character = finding_flame(word_count)
    flame_definer(person1, person2, flame_character)


# Extracting Words from names ###
def count_letters(person1, person2):
    common_characters = list(set(person1).intersection(set(person2)))
    for character in common_characters:
        person1 = person1.replace(character, '')
        person2 = person2.replace(character, '')
    word_length = len(person1 + person2)
    return word_length


# TODO: flames logic and printing the flame character
# Flames Logic
def finding_flame(word_length):
    flame_word = 'FLAME'
    if word_length > 5:
        flame_value = word_length - 5
    else:
        flame_value = word_length
    return(flame_word[flame_value - 1])


def flame_definer(person1, person2, flame_character):
    if flame_character == 'F':
        print(f"{person1} and {person2} are destined to be Friends")
    elif flame_character == 'L':
        print(f"{person1} and {person2} are destined to be Lovers")
    elif flame_character == 'A':
        print(f"{person1} and {person2} are destined to be Affectionate")
    elif flame_character == 'M':
        print(f"{person1} and {person2} are destined to be Married")
    elif flame_character == 'E':
        print(f"{person1} and {person2} are destined to be Enemies")


user_input()
