# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        previous = None
        current = slow
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        left = head
        right = previous
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

values = input().strip()
values = list(map(int, values.strip("[]").split(","))) if values != "[]" else []

head = None
prev = None
for v in values:
    node = ListNode(v)
    if not head:
        head = node
    else:
        prev.next = node
    prev = node

print(Solution().isPalindrome(head))
