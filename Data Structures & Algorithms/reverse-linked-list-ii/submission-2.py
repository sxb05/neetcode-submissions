# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prevleft, cur = dummy, head


        for _ in range(left - 1):
            prevleft, cur = cur, cur.next

        prev = None
        for _ in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        prevleft.next.next = cur
        prevleft.next = prev

        return dummy.next

        

        # prev = None
        # curr = head
        # n = left
        # while curr:
        #     if n <= n-1:
        #         temp = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = temp
        #         n += 1
        #     else:
        #         break
        #     # print(head)
        # return curr
        