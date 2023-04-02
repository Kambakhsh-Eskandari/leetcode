class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n+1)
        off = 1

        for i in range(1,n+1):
            if off * 2 == i:
                off = i
            ans[i] = 1 + ans[i - off]

        return ans
        