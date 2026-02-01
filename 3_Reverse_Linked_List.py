class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        previous = None
        current = head

        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        return previous

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

res = Solution().reverseList(head)

out = []
while res:
    out.append(res.val)
    res = res.next

print(out)
