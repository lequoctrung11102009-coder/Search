#tìm tuần tự
so_nguyen_to= [2,3,5,7,11]
def linear_search(arr, target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
vi_tri= linear_search(so_nguyen_to, 7)
print(vi_tri)
