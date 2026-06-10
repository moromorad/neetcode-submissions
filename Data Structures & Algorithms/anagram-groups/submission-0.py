class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = {}
        for s in strs:
            vals = [0] *26
            for c in s:
                vals[ord(c) - ord("a")] += 1
            if tuple(vals) in sol:
                sol[tuple(vals)].append(s)
            else:
                sol[tuple(vals)] = [s]
        return list(sol.values())
            

