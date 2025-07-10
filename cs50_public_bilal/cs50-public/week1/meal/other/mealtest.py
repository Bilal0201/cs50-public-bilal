def convert(time):
    time = time.replace(":", ".")
    hour , min = time.split(".")
    hour, min = float(hour), float(min)/60
    time = hour + min
    return time


time = input("enter time ")
print(convert(time))




 if ampm == "am" and 12.0 <= time:
        time = time - 12 #deals with the case when time is 12 am and converts it into 0.min
    elif ampm == "am" and time < 12.0: # returns the morning time as its same in 12 hour and 24 hour expt for 12am
        return time
    elif ampm == "pm" and time < 1.0: # returns afternoon time of 12 as its same in 12 hour and 24 hour
        return time
    else:
