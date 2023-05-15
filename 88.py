def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
sorted_list = [2, 5, 7, 10, 13, 17, 21]
search_item = 10

index = binary_search(sorted_list, search_item)
print("Index:", index)
