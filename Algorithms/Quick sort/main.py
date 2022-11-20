# pivot form the last
def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr

    pivot = arr.pop()
    items_greater = []
    items_smaller = []
    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_smaller.append(item)
    return quick_sort(items_smaller) + [pivot] + quick_sort(items_greater)


list = list(map(int, input().split(" ")))
print(quick_sort(list))
