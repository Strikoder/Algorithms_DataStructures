def Bubble_sort(unsorted_list):
    swapped_atleast_once = False
    for i in range(len(unsorted_list) - 1):
        for j in range(len(unsorted_list) - 1 - i):
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i+1], unsorted_list[i] = unsorted_list[i], unsorted_list[i+1]
                swapped_atleast_once = True
        if not swapped_atleast_once:
            break
    print(unsorted_list)


unsorted_list = list(map(int, input("Please enter the elements to sort: ").split()))
Bubble_sort(unsorted_list)
