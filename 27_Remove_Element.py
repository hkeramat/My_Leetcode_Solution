class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count =0
        for i,value in enumerate(nums):
            if value != val:
                nums[count] = value
                count +=1
        return count
