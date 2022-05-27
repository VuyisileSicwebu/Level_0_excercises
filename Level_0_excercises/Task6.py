                #TASK 0.6


def maximum(number_1 , number_2 , number_3):
    largest = 0
    if largest < number_1 :
        largest = number_1
        if ( largest < number_2):
            largest = number_2
            if ( largest < number_3 ):
                largest = number_3
    return largest

maximum(4, 5, 6)
maximum(91, 5, 4)
maximum(5, 12, 8)
