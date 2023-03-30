class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ## gussian formula: sum[n] = (n* n+1) / 2

        total_sum = n * (n+1) / 2

        return total_sum - sum(nums)