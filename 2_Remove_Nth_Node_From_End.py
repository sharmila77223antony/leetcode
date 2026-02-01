class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

values = input().strip()  
n = int(input().strip())  

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

res = Solution().removeNthFromEnd(head, n)

out = []
while res:
    out.append(res.val)
    res = res.next

print(out)
