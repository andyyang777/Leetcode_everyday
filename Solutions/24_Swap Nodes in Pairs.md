## 24. Swap Nodes in Pairs

### Details

- 题目链接：https://leetcode.com/problems/swap-nodes-in-pairs/

### Description

```
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
```

### Solution

```Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
# 链表，ListNode的输出方式就是指向第一个元素输出即可，所以一般要在开头就定一个不会改变的指针指向开头
        dummy = d = ListNode(0)
        
        d.next = head  # 要在while里定义p和q，因为这两个值是需要更新的
        while d.next and d.next.next:
            p = d.next
            q = p.next
            
            p.next, q.next, d.next = q.next, p, q
            d = p
            
        return dummy.next
```
