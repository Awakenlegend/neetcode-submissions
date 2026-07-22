# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, l, r):

        if l > r:
            return None

        if l == r:
            return lists[l]

        mid = (l + r) // 2

        left = self.merge(lists, l, mid)
        right = self.merge(lists, mid + 1, r)

        return self.mergeTwo(left, right)

    def mergeTwo(self, l1, l2):

        dummy = ListNode()
        tail = dummy

        while l1 and l2:

            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return dummy.next