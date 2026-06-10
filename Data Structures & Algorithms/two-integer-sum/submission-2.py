class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            t = target - nums[i]
            if t in nums:
                for j in range(len(nums)):
                    if nums[j] == t and j != i:
                        sol = [i,j]
                        return sol;
        

        