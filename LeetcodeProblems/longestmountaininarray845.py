class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        
        ret = 0
        
        for i in range(1, len(arr)-1):
            # Check if current position is a peak
            if arr[i-1] < arr[i] > arr[i+1]:
                l = r = i
                # Extend left side of mountain
                while l > 0 and arr[l-1] < arr[l]:
                    l -= 1
                
                r = i
                # Extend right side of mountain
                while r < len(arr)-1 and arr[r] > arr[r+1]:
                    r += 1
                
                # Calculate mountain length and update result
                ret = max(ret, r-l+1)
        
        return ret