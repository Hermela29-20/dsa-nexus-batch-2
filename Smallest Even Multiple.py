class Solution(object):
    def smallestEvenMultiple(self, n):
        a=n*2
        if n%2==0:
            return min(a,n)
        return a
    
