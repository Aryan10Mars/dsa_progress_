# https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        
        platform_needed = 1
        result = 1
        i = 1
        j = 0
        
        while i < n and j < n :
            if arr[i] <= dep[j]:
                platform_needed = platform_needed + 1
                i = i + 1
                
                result = max(result, platform_needed)
            
            else:
                platform_needed = platform_needed - 1
                j = j + 1
        
        return result