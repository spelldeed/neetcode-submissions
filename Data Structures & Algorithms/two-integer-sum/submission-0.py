class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # nums.sort()
        # for x in range(len(nums)):
        #     for y in range(x+1, len(nums)):
                
        #         if nums[x] + nums[y] == target:
        #             return[x] + [y]
        
        num_dict = {}
        for i, ele in enumerate(nums):
            residual = target-ele
            if residual in num_dict:
                return [num_dict[residual]] + [i]
            num_dict[ele] = i


        
        

        