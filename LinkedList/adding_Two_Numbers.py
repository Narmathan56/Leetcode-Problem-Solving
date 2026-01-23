
# Problem: Add Two Numbers
# LeetCode: https://leetcode.com/Narmathan26
# Solved by Narmathan
#Source: Youtube







# Definition for singly-linked list.



# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        l3=dummy

        carry=0
        
        while(l1 or l2):
           if l1:
            x=l1.val 
           else:x=0
           if l2:
            y=l2.val 
           else:y=0

           
           total=x+y+carry
           carry=total//10
           l3.next=ListNode(total%10)
            
           l3=l3.next
           if l1: 
            l1=l1.next
           if l2: 
            l2=l2.next

        if carry>0:
            l3.next=ListNode(carry)
        return dummy.next    

            



            
        
