# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_for_l1 = 0
        sum_for_l2 = 0
        multiply = 1

        current_node = l1
        while current_node:
            sum_for_l1 = sum_for_l1 + (current_node.val * multiply)
            multiply = multiply * 10
            current_node = current_node.next

        multiply = 1

        current_node = l2
        while current_node:
            sum_for_l2 = sum_for_l2 + (current_node.val * multiply)
            multiply = multiply * 10
            current_node = current_node.next

        r = sum_for_l1 + sum_for_l2
        arr = []

        for i in range(len(str(r))):
            arr.append(int(str(r)[i]))

        arr.reverse()

        if not arr:
            return None

        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next

        return head



s = Solution()

if __name__ == "__main__":
    list1 = ListNode(3, ListNode(7, ListNode(2)))
    list2 = ListNode(5, ListNode(1, ListNode(9)))

    print(s.addTwoNumbers(list1, list2))

