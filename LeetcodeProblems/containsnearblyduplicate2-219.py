class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Use a sliding window approach with a set to track elements
        seen = set()
        for i, num in enumerate(nums):
            # If we find a duplicate within the window, return True
            if num in seen:
                return True
            # Add current number to our set
            seen.add(num)
            # If window size exceeds k, remove the earliest element
            if len(seen) > k:
                seen.remove(nums[i - k])
        # No duplicates found within window of size k
        return False
