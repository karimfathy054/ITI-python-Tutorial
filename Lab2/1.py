def reduce(list_in):
    ans = [list_in[0]]
    for i in range(1,len(list_in)):
        if list_in[i]==list_in[i-1]:
            continue
        else:
            ans.append(list_in[i])
    return ans

a = [1,1,1,2,2,3,3,3,3,4,5,5]

print(reduce(a))
            
            