class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for i in range(len(nums)):
            if vals.get(nums[i],0) != 0:
                return True
            vals[nums[i]] = 1
        return False

        