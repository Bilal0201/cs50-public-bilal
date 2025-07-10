def convert(sen):
    sen = sen.replace(":)" , "🙂")
    sen = sen.replace(":(" , "🙁")
    return sen
def main():
    line = input("enter a sentence")
    line = convert(line)
    print (line)

main()
