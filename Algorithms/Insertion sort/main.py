def insertion_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        anchor = unsorted_list[i]
        j = i - 1
        while j >= 0 and anchor < unsorted_list[j]:
            unsorted_list[j + 1] = unsorted_list[j]
            j = j - 1
        unsorted_list[j + 1] = anchor
    print(unsorted_list)

unsortred_list = list(map(int,input("Please enter your list:").split()))
insertion_sort(unsortred_list)
