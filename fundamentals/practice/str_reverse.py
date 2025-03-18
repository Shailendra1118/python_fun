from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        #last_index = len(s)-1
        self.reverseUtil(s, 0)
        print(f"reversed string: {s}")
    
    def reverseUtil(self, s: List[str], curr:int) -> None:
        if curr >= len(s):
            return
        self.reverseUtil(s, curr+1)
        temp = s[curr]
        indx = len(s)-1-curr
        s[curr] = s[indx]
        s[indx] = temp

sol = Solution()
input = ["h","e","l","l","o"]
sol.reverseString(input)
