def selection_sort(values):
    size = len(values)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1, size):
            if values[j] < values[min_index]:
                min_index = j
        # Swapping elements
        values[i], values[min_index] = values[min_index], values[i]


elements = list(map(int, input().split()))
selection_sort(elements)
print(elements)
