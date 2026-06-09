def buuble_sort(list_in):
    for i in range(len(list_in)):
        for j in range(len(list_in)-i-1):
            if list_in[j]>list_in[j+1]:
                list_in[j],list_in[j+1] = list_in[j+1],list_in[j]
    return list_in

a = [5,4,3,2,1]
print(buuble_sort(a))