# Time Complexity: O(n log n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, v in enumerate(nums):
            if i != v:
                return i
        return len(nums)

# Time Complexity: O(n)
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

# Time Complexity: O(n)
class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)

# Time Complexity: O(n)
class Solution4:
    def missingNumber(self, nums: List[int]) -> int:
        from functools import reduce
        from operator import xor
        return reduce(xor, nums + list(range(len(nums) + 1)))
