class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx1 = 0
        idx2 = 0
        n1 = len(word1)
        n2 = len(word2)
        output = ""
        while idx1 < n1 or idx2 < n2:
            if idx2 == n2:
                output += word1[idx1]
                idx1 += 1
                continue 
            if idx1 == n1:
                output += word2[idx2]
                idx2 += 1
                continue 
            output += word1[idx1]
            output += word2[idx2]
            idx1 += 1
            idx2 += 1
        return output 
