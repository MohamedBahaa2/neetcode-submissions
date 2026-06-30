class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_clean = set(nums)

        return len(nums) != len(nums_clean) 
        