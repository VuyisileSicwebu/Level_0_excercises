                 #TASK 0.8
                 
def time_convertor(time):
    hours = time//60 
    minutes = time%60
    if hours <= 1 and minutes == 1:
        return str(hours) + " hour " + str(minutes) + " minute"
    elif hours <= 1 and minutes > 1:
        return str(hours) + " hour " + str(minutes) + " minutes"
    elif hours > 1 and minutes == 1:
        return str(hours) + " hours " + str(minutes) + " minute"
    elif hours > 1 and minutes > 1:
        return str(hours) + " hours " + str(minutes) + " minutes"

time_convertor(58)
time_convertor(61)
time_convertor(121)
time_convertor(132)
