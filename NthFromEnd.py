'''Problem description:
The core is to implement a fast 2-pointer to solve 2-sum, and recursion to reduce the N-sum to 2-sum. 
Some optimization was be made knowing the list is sorted

Examples:
   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
 Given n will always be valid.
 Try to do this in one pass. 
 '''
#recursively determine the indexes again, but this time my helper function removes the nth node
class Solution:
    def removeNthFromEnd(self, head, n):
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]

   #without a dummy extra node, simply handle the special case of removing the head right after the fast cursor got its head start
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head