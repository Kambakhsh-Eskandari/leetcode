class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one, two = 1, 1
        c = 0
        for n in range(n -1):
            c = one + two
            two = one
            one = c
        
        return one