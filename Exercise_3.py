def quicksort(A, return_num_comp=False, num_comp=0):
    """Implementation of the QuickSort Algorithm for Python lists."""

    n_A = len(A)
    num_comp += max(n_A - 1, 0)

    if n_A <= 1:
        if return_num_comp:
            return A, num_comp
        else:
            return A
    else:
        # Select pivot index and swap the pivot element with the first element
        # of the list
        if n_A % 2 == 0:
            median_of_three = [A[0], A[n_A // 2 - 1], A[-1]]
            pivot_value = merge_sort(median_of_three)[1]
        else:
            median_of_three = [A[0], A[n_A // 2], A[-1]]
            pivot_value = merge_sort(median_of_three)[1]

        if median_of_three.index(pivot_value) == 0:
            pivot_index = 0
        elif median_of_three.index(pivot_value) == 1:
            if n_A % 2 == 0:
                pivot_index = n_A // 2 - 1
            else:
                pivot_index = n_A // 2
        else:
            pivot_index = -1

        A[0], A[pivot_index] = A[pivot_index], A[0]

        # Partition the list around the pivot element
        i = 1
        for j in range(1, n_A):
            if A[j] < A[0]:
                A[i], A[j] = A[j], A[i]
                i += 1
        A[0], A[i - 1] = A[i - 1], A[0]

        # Recursively sort the parts left and right of the pivot element
        A[:i - 1], num_comp = quicksort(A[:i - 1], True, num_comp)
        A[i:], num_comp = quicksort(A[i:], True, num_comp)

        if return_num_comp:
            return A, num_comp
        else:
            return A


def merge_sort(A):
    """Implementation of the Merge Sort Algorithm for Python lists."""

    n_A = len(A)

    if n_A == 1:
        return A
    else:
        sorted_left_half = merge_sort(A[:n_A // 2])
        sorted_right_half = merge_sort(A[n_A // 2:])

        i = 0
        j = 0
        merged_result = []
        for k in range(n_A):
            if i == len(sorted_left_half):
                merged_result.append(sorted_right_half[j])
                j += 1
                continue

            if j == len(sorted_right_half):
                merged_result.append(sorted_left_half[i])
                i += 1
                continue

            if sorted_left_half[i] <= sorted_right_half[j]:
                merged_result.append(sorted_left_half[i])
                i += 1
            else:
                merged_result.append(sorted_right_half[j])
                j += 1

        return merged_result


if __name__ == '__main__':
    with open('QuickSort.txt', 'r') as f:
        list_quicksort = [int(x.strip()) for x in f.readlines()]
    print("The total number of comparisons made to sort the numbers in the "
          "file 'QuickSort.txt' is: {0}".format(
              quicksort(list_quicksort, True)[1]))
