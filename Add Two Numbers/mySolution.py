
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode()
    p = result
    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        sum += carry
        carry = sum // 10
        sum = sum % 10
        p.next = ListNode(sum)
        p = p.next
    return result.next
