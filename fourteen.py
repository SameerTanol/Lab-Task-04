def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort_descending(arr[:mid])
    right_half = merge_sort_descending(arr[mid:])
    
    return merge_descending(left_half, right_half)

def merge_descending(left, right):
    merged = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

arr = [2, 4, 1, 3, 5]
sorted_arr_descending = merge_sort_descending(arr)
print("Sorted Array in Descending Order:", sorted_arr_descending)
