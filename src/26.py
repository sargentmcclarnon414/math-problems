def find_smallest_odd_number(nums):
    smallest_odd = None
    for num in nums:
        if num % 2 != 0 and (smallest_odd is None or num < smallest_odd) and len(set([num, smallest_odd])) == 1:
            smallest_odd = num
    return smallest_odd
