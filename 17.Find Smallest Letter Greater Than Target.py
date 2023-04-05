class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        
        if letters[0] > target or letters[-1] <= target:
            return letters[0]

        l, r = 0, len(letters) - 1

        while l<=r:
            mid = (l+r) // 2
            if target >= letters[mid]:
                l = mid + 1

            if target < letters[mid]:
                r = mid - 1

        return letters[l] 