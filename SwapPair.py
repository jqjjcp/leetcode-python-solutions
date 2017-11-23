'''Problem description:
Given a linked list, swap every two adjacent nodes and return its head. 

Examples,
 Given 1->2->3->4, you should return the list as 2->1->4->3. 
Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed. 

Here, pre is the previous node. Since the head doesn't have a previous node, I just use self instead. Again, a is the current node and b is the next node.
To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, we need to change those three references. Instead of thinking about in what order I change them, I just change all three at once.
‘’‘
def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next


