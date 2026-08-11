class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        num_size = len(nums)
        return nums[int(num_size/2)] if num_size % 2 == 0 else nums[int((num_size-1)/2)]
        