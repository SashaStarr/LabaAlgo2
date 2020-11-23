

def find_numbers(array,sum):

    """
        :param array: array of numbers to find
        :param sum: required sum
        :return: returning answer Andrew
        >>> find_numbers([1,2,3,4,5],9)
        YES
        >>> find_numbers([2,3,4,5,6],1)
        NO
        >>> find_numbers([20,30,40,50],100)
        YES
        >>> find_numbers([3,3,3], 8)
        NO
    """

    length = len(array)
    if length >= 1000 or length < 3 or sum >= 3 * pow(10, 9):
        return
    quick_sort(array, 0, length - 1)
    for i in range(0, length - 2):
        first_element = i + 1
        last_element = length - 1
        while first_element < last_element:
            if array[i] + array[first_element] + array[last_element] == sum:
                return print("YES")
            elif array[i] + array[first_element] + array[last_element] < sum:
                first_element += 1
            else:
                last_element -= 1
    return print('NO')


def quick_sort(array, low, high):
        """
        :param array: array of numbers to sort
        :param low: first element of array
        :param high: last element of array
        :return: returning sorted array
        >>> quick_sort([12,1,4,3,5,4,5,6,1], 0, 8)
        [1, 1, 3, 4, 4, 5, 5, 6, 12]
        """
        if low < high:
            split_index = partition(array, low, high)
            quick_sort(array, low, split_index)
            quick_sort(array, split_index + 1, high)

        return array

def partition(array, low, high):
    pivot = array[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]

if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)