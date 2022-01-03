def even_odd_counter(arr_values):
    count_even=0
    count_odd=0

    even_odd = []

    for i in range(len(arr_values)):
        if(arr_values[i] % 2 == 0):
            count_even+=1
        else:
            count_odd+=1
    
    even_odd.append(count_even)
    even_odd.append(count_odd)


    print("Even: {} | odd: {}".format(even_odd[0],even_odd[1]))


even_odd_counter([23,8,3,6,7,9,10,20,35,45,50,62])
