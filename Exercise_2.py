def count_inversions(A):
    """Implementation of the Count Inversions Algorithm for Python lists."""

    n_A = len(A)

    if n_A == 1:
        return A, 0
    else:
        sorted_left_half, left_inversions = count_inversions(A[:n_A // 2])
        sorted_right_half, right_inversions = count_inversions(A[n_A // 2:])

        i = 0
        j = 0
        split_inversions = 0
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
                split_inversions += len(sorted_left_half) - i
                j += 1

        return merged_result, left_inversions + right_inversions \
            + split_inversions


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
    with open('IntegerArray.txt', 'r') as f:
        list_count_inversions = [int(x.strip()) for x in f.readlines()]
    print("The number of inversions in the file 'IntegerArray.txt' is: "
          "{0}".format(count_inversions(list_count_inversions)[1]))
