def main():
    bal = 50
    print("Amount due: 50")
    while True:
        coin = valid_input(bal)
        bal = bal -coin
        if bal <= 0:
            print("Change Owed:", bal*-1)
            break
        else:
            print(f"Amount Due: {bal}")

def valid_input(bal):
     while True:
        coin = int(input("Insert Coin: "))
        if coin in [5, 10 , 25]:
            return coin
        else: print("Amount Due:", bal)


main()
