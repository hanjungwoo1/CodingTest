class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head = ListNode(None)
tail = ListNode(None)
head.right = 5
print(head.right)