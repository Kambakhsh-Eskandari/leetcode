
## First solution:
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        s = 0
        for num in range(left, right+1):
            s = s + self.array[num]
        return s
    
## second solution:

import numpy as np
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = [0] + list(np.cumsum(nums))
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.arr[right+1] - self.arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


