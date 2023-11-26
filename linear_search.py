def linear_search(list,taret):
    for i in range(len(list)):
        if list[i] == taret:
            return i
    return -1

list = [1,2,3,4,5,6,7,8,9,]
t = 10
print(linear_search(list,t))