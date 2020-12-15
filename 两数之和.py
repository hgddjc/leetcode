class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        这是第一道题，一开始我用了两个for的暴力循环，提交发现是超时的，
        后来看了题目下面别人的评论知道了这种方法，可以用字典
        """
        hashmap = {}

        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
