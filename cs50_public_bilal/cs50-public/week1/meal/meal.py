def main():
    my_time = input("What time is it? ")
    my_time = convert(my_time)
    if 7.0 <= my_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= my_time <= 13.0:
        print("lunch time")
    elif 18.0 <= my_time <= 19.0:
        print("dinner time")
    else: print("")





def convert(time):
    hour , min = time.split(":")
    hour, min = float(hour), float(min)/60
    time = hour + min
    return time



if __name__ == "__main__":
    main()
