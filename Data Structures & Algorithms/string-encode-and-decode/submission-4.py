class Solution:

    def encode(self, strs: List[str]) -> str:
        
        sol = ""
        for s in strs:
            sol = f"{sol}{len(s)}#{s}"
        return sol 

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i != len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            wordLength = int(s[i:j])
            word = s[j + 1:j + 1 + wordLength]
            strs.append(word)
            i = j + 1 + wordLength
        return strs

             