class Solution(object):
    def reverse(self, x):
        import sys
        """
        :type x: int
        :rtype: int
        """
        if x> 0:
            a =int(str(x)[::-1])
            
        else:
            a = -int(str(abs(x))[::-1])
            
        max = 2**31
        
        if abs(a) > max:
            
            return 0
        else:
            return a
