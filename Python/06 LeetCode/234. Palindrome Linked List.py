# Given the head of a singly linked list, return true if it is a palindrome.


from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = head
        b = []
        while a != None:
            b.append(a.val)
            a = a.next
        return b == b[::-1]


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)
n4 = ListNode(1)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = None

a = Solution
assert a.isPalindrome(a, head=n1) == True
