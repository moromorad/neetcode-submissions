class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        pos = [1] * len(nums)
        prod = 1
        for i in range(len(nums)):
            pre[i] = prod
            prod = prod * nums[i]
        
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            pos[i] = prod
            prod = prod * nums[i]

        sol = [0] * len(nums)
        for i in range(len(nums)):
            sol[i] = pre[i] * pos[i]
        return sol