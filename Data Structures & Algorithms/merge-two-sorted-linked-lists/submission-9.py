# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node_temp = temp = ListNode()
        if list1 is None:
            return list2
        if list2 is None:
            return list1


        while list1 and list2:
            if list2.val > list1.val:
                temp.next = list1 
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        temp.next = list1 or list2
        return node_temp.next


            

        