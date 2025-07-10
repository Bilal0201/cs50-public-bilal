def main():
    camel_case = input("camelCase: ") #prompts the user to enter a camel case which is then stored to the variable camel_case
    print(f"snake_case: {get_snake_case(camel_case)}") #prints the prompt and the result from the function


def get_snake_case(name):
    new_name = "" #intializes the new name to empty string
    for letter in name: #iterates for every letter in the string
        if letter.isupper(): #checks if letter is capital
            new_name = new_name + "_" + letter.lower() #adds a underscore in the existing string followed by the letter in lower case
        else: new_name =  new_name + letter #as it is adds the letter in the existing string
    return new_name #returns the updated string


main()
