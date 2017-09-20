"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.
"""


def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    i, j = 0, len(numbers)-1
    s = numbers[i] + numbers[j]  
    while i < j:
        if s == target:
            return [i+1, j+1]
        elif s < target:
            s += numbers[i+1] - numbers[i]
            i += 1
        else:
            s += numbers[j-1] - numbers[j]
            j -= 1