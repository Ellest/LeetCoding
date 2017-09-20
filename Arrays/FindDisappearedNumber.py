"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array)
, some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.
"""


def findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    for n in nums:
        val = abs(n)
        if nums[val-1] > 0: nums[val-1] *= -1
    for i,v in enumerate(nums):
        if v > 0: res.append(i+1)
    return res