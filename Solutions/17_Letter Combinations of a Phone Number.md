## 17. Letter Combinations of a Phone Number

### Details

- 题目链接：https://leetcode.com/problems/letter-combinations-of-a-phone-number/

### Description

```
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
```

### Solution

```Python3
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        :type digits: string
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        
        digit_map = {
            0: "0", 1: "1", 2: "abc",
            3: "def", 4: "ghi", 5: "jkl",
            6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
        }
        
        result = [""]
        
        for digit in digits:
            tmp_list = []
            for ch in digit_map[int(digit)]:
                #读进来的时候是一个string，要用int将其转换为int
                for str in result:
                    tmp_list.append(str + ch)
            result = tmp_list
        return result
    
    
        # round 1 - read '2' 需要在自己的abc里，先循环读到每个字母，这里有一个循环
        #           possible output: tem_list = ["a", "b", "c"]
        #           result = tmp_list
        # round 2 - read '3'需要在def里自己先做循环，将每个值读到，这里是第二个循环，假设读到d，那么又要在前一步的result里做一个循环，分别fetch出来ad，bd，cd
        #           possible fetch ch: ["d", "e", "f"],这个是第二个循环
        #           result + fetch match => 想要的output，要把result和fetch出来的值相匹配
        
        # 所以总的需要三个循环
```
