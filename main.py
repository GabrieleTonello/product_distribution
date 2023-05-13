
GLOBAL_MODULE = 1000000007

def quick_sort(array:list[int]):
    """
    This function is an implementation of quick sort algorithm 

    :param array (list[int]): the array that is going to be ordered 
    :return : each time return an array with the pivot at its correct position
    """
    if len(array) > 1:
        piv = len(array) // 2
        val = array[piv]
        left = [i for i in array if i < val] # creates an array with all the numbers that are minor than the pivot
        mid = [i for i in array if i == val] # creates an array with all the numbers that are equal to the pivot
        right = [i for i in array if i > val] # creates an array with all the numbers that are grater than the pivot
        return quick_sort(left) + mid + quick_sort(right) 
    else:
        return array

def product_allocation(array1: list[int], array2: list[int]):
    """ 
    This function has to maximize the product allocation. In order to do that, first it orders the array and then calculates 
    the product allocation as defined in the task description.

    :param array1 (list[int]): the first line, which contains 2 integers: n and m
    :param array2 (list[int]): the second line, which contains n integers
    :return sum (int): sum of each value in each segment, multiplied for the segment value
    """
    if array1[1] > array1[0]: # m <= n
        raise ValueError("M has to be smaller than n!")
    
    array2_ordered = quick_sort(array2) # order the array
    number_full_segment = array1[0] // array1[1] # number of segments needed
    rest = array1[0] % array1[1] # if there's any rest, it means that the last segment will have more than m elements 
    if rest > 0:
        number_full_segment -= 1 # decreases the number of full segments if rest != 0 because the last one hasn't at least m segments
    left, right = 0, array1[1] # inizializates the first segment
    sum = 0
    for segment_index in range(1, number_full_segment +1  ):
        for element in array2_ordered[left:right]: # sums every element in the segment and multiplies it by the segment_index
            sum += element * segment_index
        left += array1[1] # moves the extrem to go to the following segment
        right += array1[1]
    if rest > 0: # case when the last segment has more than m elements
        for element in array2_ordered[left:]:
            sum += element * (number_full_segment +1)
    return sum % GLOBAL_MODULE # return the maximum sum of product allocation

            

