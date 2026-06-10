class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        buckets = [[] for x in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)
        sol = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                sol.append(num)
                if len(sol) == k:
                    return sol