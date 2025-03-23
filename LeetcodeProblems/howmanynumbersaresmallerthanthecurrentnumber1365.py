class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d = {}
        for i, v in enumerate(temp):
            if v not in d:
                d[v] = i
        ret=[]
        for i in nums:
            ret.append(d[i])
        return ret

# Alternative solution using counting sort
# Time Complexity: O(n + k) where k is the range of values
class Solution2:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:        # Initialize count array with zeros (assuming constraints: 0 <= nums[i] <= 100)
        count = [0] * 102

        # Count occurrences of each number
        for num in nums:
            count[num+1] += 1
        
        # Calculate cumulative count
        for i in range(1, 102):
            count[i] += count[i-1]
        
        # For each number, its count[num] represents how many numbers are smaller than it
        return [count[num] for num in nums]
