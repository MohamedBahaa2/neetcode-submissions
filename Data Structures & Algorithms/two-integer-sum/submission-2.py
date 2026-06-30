class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = list()
        for i in range(len(nums)):
            twin = target - nums[i]

            if twin in nums:
                j = nums.index(twin)
                if i != j and not output:
                    output.append(i)
                    output.append(j)

        return sorted(output)

