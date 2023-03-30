class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for num in range(len(nums)):
            index = abs(nums[num]) - 1
            nums[index] = -abs(nums[index])

        ans =  []

        for num in range(len(nums)):
            if nums[num] > 0:
                ans.append(num+1)
        return ans