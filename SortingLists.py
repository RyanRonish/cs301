def insertion_sort(values):
    for x in range(1, len(values)):
        key = values[x]
        y = x - 1
        while y >= 0 and values[y] > key:
            values[y + 1] = values[y]
            y -= 1
        values[y + 1] = key

    return values


values = [12, 435, 132, 5, 6, 234, 576, 567]
sorted_arr = insertion_sort(values)
print(sorted_arr)

# Big O Notaion = O(N^2) because of the while loop inside of the for loop

def bubble_sort(lst):
    # Unordered list
    #my_list = [10, 6, 3, 5, 7, 2, 1, 9, 8, 4]  

    # Runs through the list multiple times
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            # Compares pairs of adjacent elements
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp


my_list = [10, 6, 3, 5, 7, 2, 1, 9, 8, 4] 
# Call for after the list is in order
bubble_sort(my_list)

print(my_list)

# The worst-case Big O running time for this code is O(N^2) due to there being a for loop, which takes n times to run through, as well as a nested for loop; this causes an NXN scenario (all other runtimes would be negligent as this is the largest Big O in the code)

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


numbers2 = [16, 64, 78, 17, 34, 54, 92, 3, 63, 10]
sorted_numbers2 = selection_sort(numbers2)
print("Sorted numbers:", sorted_numbers2)

# The worst case run time for selection sort is O(n^2) because for each iteration of the outer loop it searches for the minimum element in the unsorted portion of the array. It also needs to perform comparisons and swap each element in the array.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
   
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])


    return merge(left, right)




def merge(left, right):
    merged = []
    left_index = right_index = 0


    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1


    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged




numbers = [18, 46, 27, 17, 19, 5, 9, 32, 63, 10]
sorted_numbers = merge_sort(numbers)
print("Sorted numbers:", sorted_numbers)

# The worst case run time for this is (n log n) Since the length is getting cut in half every time to then be sorted. The second term O(n) represents the time taken to merge the two sorted halves.