def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    a = first_two_letter(s)
    b = length(s)
    c = extras(s)
    d = formatnew(s)
    f = zero_check(s)
    return a and b and c and d and f


def first_two_letter(s): #First two digits are letters
    if s[0:2].isalpha():
        return True
    else: return False

def length(s): #plate is minimum 2 digit and maximum 6 digit
    if 2 <= len(s) <= 6:
        return True
    else: return False

def extras(s):# plate doesnt conatin any special characters like .,!
    for char in s:
        if char in [".", " ", "!"]:
            return False
    return True

def format(s): #DEAD FUNCTION. DOESNT DO ANYTHING IN PROGRAM, JUST Didnt WANT TO DELETE IT :)
    if s.isalpha():
        return True
    elif s[-1].isalpha():
        return False

    else: return True

def zero_check(s): #first number is not 0
    num_count = 0
    for char in s:
        if char == "0" and num_count == 0:
            return False
        elif char.isdigit():
            num_count += 1
    return True

def formatnew(s): #numbers appear at end. no letter after a number
    for i in range(len(s)-1):
        if s[i].isdigit() and s[i+1].isalpha():
            return False
    return True

main()
