# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """stack=[]
        temp=head
        while temp:
            while stack and stack[-1].val <temp.val:
                stack.pop()
            stack.append(temp)
            temp=temp.next
        for i in range(len(stack)-1):
            stack[i].next=stack[i+1]
        stack[-1].next=None
        return stack[0]"""
        head=self.reverse(head)
        temp=head
        max_so_far=head.val
        while temp and temp.next:
            if temp.next.val<max_so_far:
                temp.next=temp.next.next
            else:
                temp=temp.next
                max_so_far=temp.val
        return self.reverse(head)


        
