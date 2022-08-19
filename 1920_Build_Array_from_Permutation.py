class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans =[0 for i in enumerate(nums)]
        for i, value in enumerate(nums):
            ans[i] = nums[nums[i]]
        return ans
