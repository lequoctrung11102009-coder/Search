def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] > target:
            right=  mid - 1
        elif arr[mid] < target:
            left = mid +1
        else:
            return mid
    return -1
arr = [1,3,6,3,7,4,9,8,34]
arr.sort()
print(arr)
tim_vi_tri= binary_search(arr,8)
print(tim_vi_tri)
