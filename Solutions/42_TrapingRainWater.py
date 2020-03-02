# Given n non-negative integers representing an elevation map where the width of
#  each bar is 1, compute how much water it is able to trap after raining. 
# 
#  
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In 
# this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos
#  for contributing this image! 
# 
#  Example: 
# 
#  
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6 
#  Related Topics Array Two Pointers Stack


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        if height == 0 or len(height) < 3:
            return 0
        sum = 0
        leftmax = 0
        rightmax = 0
        i = 0
        j = len(height) -1
        while (i < j):
            leftmax = max(leftmax, height[i])
            rightmax = max(rightmax, height[j])
            if (leftmax < rightmax):
                sum += leftmax-height[i]
                i = i +1
            else:
                sum += rightmax - height[j]
                j = j-1
        return sum

# leetcode submit region end(Prohibit modification and deletion)
