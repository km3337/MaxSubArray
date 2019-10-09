"""
Practicing recursion/Divide and Conquer. This is a  take on the maximum sub Array problem.
"""


def find_cross_sub_array(arr, l, m, h):
    """
    finds the maximal cross sub array
    :param arr: list of numbers
    :param l: the "low' point in arr
    :param m:  the "middle" point in arr
    :param h: the "high" point in arr
    :return: returns the sum of cross array
    """
    total = 0; left_sum = -999999
    # grab the values on the left of the middle
    for i in range(m, l-1, -1):
        total = total + arr[i]
        if total > left_sum:
            left_sum = total

    total = 0; right_sum = -999999
    # grab the values on the right of the middle
    for i in range(m+1, h+1):
        total = total + arr[i]
        if total > right_sum:
            right_sum = total

    return left_sum + right_sum


def find_max_sub_array(arr, low, high):
    """
    Driver function that recursively calls itself on the left and right portions of an array to find the max sub array.
    finds the max "cross-subarry", the array between the left and right values.
    :param arr: list of numbers
    :param low: left boundary index in arr
    :param high: right boundary index in arr
    :return: returns the value of the maximal sub array in the given array of numbers.
    """
    if low == high:
        return arr[low]
    else:
        middle = (low + high) // 2
        return max(find_max_sub_array(arr, low, middle),
                   find_max_sub_array((arr, middle+1, high)),
                   find_cross_sub_array(arr, low, middle, high))


def main():
    test = [1, 2, 4, 6, 102, 2, -10, 20, -4]
    length = len(test)
    max_sum = find_max_sub_array()
    print(max_sum)


if __name__ == "__main__":
    main()