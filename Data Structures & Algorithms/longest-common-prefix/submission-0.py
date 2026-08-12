class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_len = min([len(curr_str) for curr_str in strs])

        for curr_idx in range(0, len(strs)-1):
            if str_len <= 0:
                return ""
            while strs[curr_idx][:str_len] != strs[curr_idx+1][:str_len]:
                str_len-=1
                if str_len <= 0:
                    return ""
        return strs[0][:str_len]
        


        