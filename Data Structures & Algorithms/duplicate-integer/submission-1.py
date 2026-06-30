class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        nums_clean = set(nums)

        return len(nums) != len(nums_clean) 
        """
        seen = set()

        for i in nums:
            if i in seen:
                return True 
            else:
                 seen.add(i)

        return False

