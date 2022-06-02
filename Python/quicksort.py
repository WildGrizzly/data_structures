from random import randint

def main():
    for _ in range(100000):
        for size in range(20):
            test = random_array(size)
            quicksorted = quicksort(test) 
            true_sort = sorted(test)
            for ele, true in zip(quicksorted, true_sort):
                if ele != true:
                    print(f'{test} : {quicksorted}')
                    continue

def random_array(length: int, maximum=100):
    return [randint(0, maximum) for _ in range(length)] 

def quicksort(arr, in_place=False):
    if not in_place:
        copy = [_ for _ in arr]
        __recur_quicksort(copy, 0, len(arr) - 1)
        return copy
    __recur_quicksort(arr, 0, len(arr) - 1)
    

def __recur_quicksort(arr, start_index, end_index):
    if start_index >= end_index:
        return
    pivot_index = pivot_subarray(arr, start_index, end_index)
    __recur_quicksort(arr, start_index, pivot_index - 1)
    __recur_quicksort(arr, pivot_index + 1, end_index)

def pivot_subarray(arr, start_index: int, end_index: int) -> int:
    pivot = arr[end_index]
    start_offset, end_offset = 0, 0
    pivot_num = 0
    while start_index + start_offset <= end_index - end_offset:
        current_left, current_right = start_index + start_offset, end_index - end_offset
        if arr[current_left] > pivot:
            if current_right - 1 != current_left:
                arr[current_right], arr[current_right - 1] = arr[current_right - 1], arr[current_right]
            arr[current_right], arr[current_left] = arr[current_left], arr[current_right]
            end_offset += 1
        else:
            if arr[current_left] == pivot:
                pivot_num += 1
            start_offset += 1

    # still need to throw elements equalling pivot to the center
    pivot_offset = 1
    pivot_loc = start_index + start_offset - 1
    for offset in range(start_offset - pivot_num):
        current_index = offset + start_index
        if arr[current_index] == pivot:
            arr[current_index], arr[pivot_loc - pivot_offset] = arr[pivot_loc - pivot_offset], arr[current_index]
            pivot_offset += 1

    return pivot_loc

if __name__ == "__main__":
    main()
