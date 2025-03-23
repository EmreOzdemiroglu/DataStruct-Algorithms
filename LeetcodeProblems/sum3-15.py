class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize result list
        triplets = []
        
        # Sort the array to make two-pointer approach work
        nums.sort()
        
        # Iterate through the array
        for idx, val in enumerate(nums):
            # Skip duplicates to avoid duplicate triplets
            if idx > 0 and val == nums[idx-1]:
                continue
                
            # Use two pointers technique for the remaining array
            left = idx + 1
            right = len(nums) - 1
            
            # Move two pointers toward each other
            while left < right:
                # Calculate current sum
                currentSum = val + nums[left] + nums[right]
                
                # If sum is zero, we found a triplet
                if currentSum == 0:
                    # Add to result
                    triplets.append([val, nums[left], nums[right]])
                    # Move left pointer and skip duplicates
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                # If sum is less than zero, increment left pointer
                elif currentSum < 0:
                    left += 1
                # If sum is greater than zero, decrement right pointer
                else:
                    right -= 1
                    
        return triplets