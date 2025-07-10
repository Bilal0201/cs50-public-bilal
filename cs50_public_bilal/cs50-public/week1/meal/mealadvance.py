def main():
    my_time = input("What time is it? ")
    if "am" in my_time or "pm" in my_time:
        my_time =  hourconvert(my_time) #converts 12 hour time
    else: my_time = convert(my_time) #converts 24 hour time

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

def hourconvert(time): #logic of function written by me, but simplified and stripped using ai, so not 100% my code
    time, ampm = time.split() # stores am or pm in ampm, and rest of time in time
    time = convert(time) # gets time in flaot and decimal to further compare
    if ampm == "am" and time >= 12.0:
        time -= 12
    elif ampm == "pm" and time < 12.0:
        time += 12
    return time




if __name__ == "__main__":
    main()
