class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict_strs = {''.join(sorted(strs[0])) : [strs[0]]}
        # dict_strs = {''.join(sorted(strs[curr_idx])) : [strs[curr_idx]] if ''.join(sorted(strs[curr_idx])) not in dict_strs.keys() else dict_strs[''.join(sorted(strs[curr_idx]))].append(strs[curr_idx]) for curr_idx in range(0, len(strs))}
        # ls = []
        # for k,v in dict_strs.items():
        #     ls.append(v)
        dict_strs = {}
        for curr_str in strs:
            sorted_str = ''.join(sorted(curr_str))
            if sorted_str not in dict_strs:
                dict_strs[sorted_str] = [curr_str]
            else :
                dict_strs[sorted_str].append(curr_str)

        ls = []
        for k,v in dict_strs.items():
            ls.append(v)

        return ls





        
        