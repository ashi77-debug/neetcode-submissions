class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     
        # if len(s) != len(t):
        #     return False
        # #1.Directly by sorting(sorted == sort)

        # return sorted(s) == sorted(t)
        
        #2.Hash Map and get function 

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(t)):
            countS[s[i]] = 1 + countS.get(s[i] , 0)

            countT[t[i]] = 1 + countT.get(t[i] , 0)

        return countS == countT

