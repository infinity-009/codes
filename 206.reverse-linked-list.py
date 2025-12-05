#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # prev      h,c      nn       

        # null <-    1     ->2     ->3     ->4     ->5

        if not head:
            return head 
        
        prev = None

        while head:

            nextnode=head.next

            head.next=prev

            prev=head

            head=nextnode

        return prev



        
# @lc code=end

