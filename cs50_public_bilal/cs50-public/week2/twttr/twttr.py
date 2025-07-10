def main():
    word = input("Input: ")
    my_word = ""
    for char in word:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            continue
        else:
            my_word += char
    print("Output:", my_word)

main()


