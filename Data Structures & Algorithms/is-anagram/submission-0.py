from collections import defaultdict
from typing import Dict
class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        # # if len(s) != len(t) :
        # #     return False

        # word_dict : Dict[str, int] = defaultdict(int)
        # for x in s:
        #     word_dict[x] +=1
        # for x in t:
        #     word_dict[x] -=1
        #     if word_dict[x] <0 :
        #         return False 
        
        # for key,val in word_dict.items():
        #     if val >= 1:
        #         return False
        # return True

        # if len(s) !=  len(t) :
        #     return False 

        arr = [0]*26 

        for idx in range(max(len(s), len(t))):
            try:
                arr[ord(s[idx]) - ord('a') ] += 1
                arr[ord(t[idx]) - ord('a') ] -= 1
            except :
                return False

        for ele in arr:
            if ele != 0 :
                return False 
        
        return True


        