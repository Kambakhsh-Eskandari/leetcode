class Solution(object):
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums,target,0,len(nums)-1)
    
    # Solution 1:
    def binarySearch(self, nums, target,low,high):
        if low > high:
            return -1
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(nums, target, mid+1, high)
        elif nums[mid] >= target:
            return self.binarySearch(nums, target, low, mid-1)
        
        
        # Solution 2:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid +1
            else:
                r = mid - 1

        return -1 
        
        