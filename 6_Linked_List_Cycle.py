class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

head_input = input("Enter head (LeetCode format): ")   
pos = int(input("Enter pos: "))                       

values = list(map(int, head_input.strip("[]").split(","))) if head_input != "[]" else []

head = None
prev = None
nodes = []

for val in values:
    node = ListNode(val)
    nodes.append(node)
    if not head:
        head = node
    else:
        prev.next = node
    prev = node

if pos != -1 and nodes:
    prev.next = nodes[pos]   

print(Solution().hasCycle(head))
