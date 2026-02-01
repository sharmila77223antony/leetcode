class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next

l1 = input().strip()  
l2 = input().strip()  

vals1 = list(map(int, l1.strip("[]").split(","))) if l1 != "[]" else []
vals2 = list(map(int, l2.strip("[]").split(","))) if l2 != "[]" else []

head1 = head2 = None
prev = None
for v in vals1:
    node = ListNode(v)
    if not head1:
        head1 = node
    else:
        prev.next = node
    prev = node

prev = None
for v in vals2:
    node = ListNode(v)
    if not head2:
        head2 = node
    else:
        prev.next = node
    prev = node

res = Solution().mergeTwoLists(head1, head2)

out = []
while res:
    out.append(res.val)
    res = res.next

print(out)
