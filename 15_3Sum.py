class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        
        for i in range(n-2):  # if the last two elements satisfy the requirements
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[n-1] + nums[n-2] < 0:
                continue
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            #for it's sorted, so if there are two same numbers, they can only be neighbours to each other.
            l = i + 1
            r = n - 1 # n-1 is the rightest, for n numbers [0, 1, ... , n-1]
            while l < r:
                tmp = nums[i] + nums[l] + nums[r] # do the algo. from both sides.
                if tmp == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l+1 < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    while l < r-1 and nums[r] == nums[r-1]:
                        r -=1
                    r -= 1
                elif tmp < 0:
                    l += 1
                else:
                    r -= 1
        return result
                
        
