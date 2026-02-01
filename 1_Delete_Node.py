class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteNode(self, node):
        if not node or not node.next:
            return  
        node.val = node.next.val
        node.next = node.next.next

values = input().strip()   
target = int(input().strip()) 

values = list(map(int, values.strip("[]").split(","))) if values != "[]" else []

head = None
prev = None
nodes = []

for v in values:
    n = ListNode(v)
    nodes.append(n)
    if not head:
        head = n
    else:
        prev.next = n
    prev = n

for n in nodes:
    if n.val == target:
        Solution().deleteNode(n)
        break

out = []
cur = head
while cur:
    out.append(cur.val)
    cur = cur.next

print(out)
