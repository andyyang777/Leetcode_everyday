## 11. Container With Most Water

### Details

- 题目链接：https://leetcode.com/problems/container-with-most-water/submissions/

### Description

```
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

### Solution

Well, this one is pretty good, and I beat 99.89% people on this question. Good work!
```Python3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #we can use two indicator, from left to right separately
        l = 0
        r = len(height)-1
        Max = 0
        
        while l < r: # cannot equal, if equal, result will be 0, time consuming
            w = r - l
            if height[l] < height[r]:
                h = height[l]
                l += 1
            else:
                h = height[r]
                r -= 1
            tem = w * h
            
            if tem > Max:
                Max = tem
        return Max
```
