def binary_search_rec(list,taret,low,high):
    if low < high:
        mid = (high+low)//2
        if list[mid] == taret:
            return mid
        elif list[mid] > taret:
            return binary_search_rec(list, taret, low, mid - 1)
        elif list[mid] < taret:
            return binary_search_rec(list, taret, mid + 1, high)
    return -1

list = [1,2,3,4,5,6,7,8,9]
t = 22
print(binary_search_rec(list,t,0,int(len(list)-1)))