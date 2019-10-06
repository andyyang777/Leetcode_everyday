## 9. Palindrome Number

### Details

- 题目链接：https://leetcode.com/problems/palindrome-number/

### Description

```
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
Well, the answer is no now. With my poor programming skills, I will have to convert it to a string, LOL. Maybe in the future I can manage to do it.
```

### Solution


```Python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False #all the negative numbers cannot be palindrome numbers.
        else:
            s = str(x)[::-1]
            if str(x) == s:
                return True
            else: 
                return False
```
