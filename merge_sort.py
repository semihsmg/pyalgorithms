def merge_sort(lst):
    print("Splitting ", lst)
    if len(lst) > 1:
        q = len(lst) // 2
        left_lst = lst[:q]
        right_lst = lst[q:]

        merge_sort(left_lst)
        merge_sort(right_lst)

        i = 0
        j = 0
        k = 0

        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst[k] = left_lst[i]
                i = i + 1
            else:
                lst[k] = right_lst[j]
                j = j + 1
            k = k + 1

        while i < len(left_lst):
            lst[k] = left_lst[i]
            i = i + 1
            k = k + 1

        while j < len(right_lst):
            lst[k] = right_lst[j]
            j = j + 1
            k = k + 1
    print('Merging: ', lst)


lst = [3, 6, 1, 5, 2, 4]

merge_sort(lst)
