def all_unique(list_in):
    return len(list_in)==len(set(list_in))

a = [1,2,3,4,5]
b = [1,2,3,4,1]
print(all_unique(a))
print(all_unique(b))
    