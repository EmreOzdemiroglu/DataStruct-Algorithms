# O(n) time complexity
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        nums_set = set(nums)

        for i in range(1, len(nums)+1):
            if not i in nums_set:
                output.append(i)

        return outputb

# o(1) space complexity - Understand it deeply later

class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # This solution uses the array itself to track which numbers appear
        
        # Step 1: Mark numbers that exist by making their corresponding indices negative
        for i in range(len(nums)):
            # Get the actual value (ignoring any negative sign) and convert to zero-indexed
            temp = abs(nums[i]) - 1
            # If the value at this index is positive, make it negative to mark that we've seen this number
            if nums[temp] > 0:
                nums[temp] *= -1
        
        # Step 2: Collect indices where values are still positive
        res = []
        for i, n in enumerate(nums):
            # If a value is still positive, it means the number (i+1) never appeared in the array
            if n > 0:
                # Convert back from zero-indexed to the actual missing number
                res.append(i+1)
        
        # Return the list of missing numbers
        return res
