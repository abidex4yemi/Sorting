# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index, len(arr)):

            if arr[j] < arr[smallest_index]:
                smallest_index = j

        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    array_length = len(arr)

    for i in range(array_length):
        for j in range(0, array_length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubble_sort([20, 10, 4, 9, 1, 0, 43]))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
