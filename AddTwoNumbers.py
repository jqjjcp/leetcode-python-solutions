'''
Problem description:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
class Solution:
# @return a ListNode
def addTwoNum(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next
'''Python supports arbitrarily large integers, 
   so turn the two lists into ints, add them, and turn the sum into a list
'''
class Solution:
    def addTwoNumbers(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n / 10)
            return node
        return tolist(toint(l1) + toint(l2))

##iterative tolist instead of recursive:

   class Solution:
       '''The chained assignment works as following: tmp = ListNode(n % 10); last.next = tmp; last = tmp;The last assignment came after the second assignment, therefore overwrite last.next as none.What you perceived is that they hold different reference and therefore can't guarantee the variable last proceed to be last.next.
        '''
        def addTwoNum（self,l1,l2):
           def toint(node):
               return node.val + 10 * toint(node.next) if node else 0
           n = toint(l1) + (l2)
           first = last = ListNode(n%10)
           #tmp = ListNode(n % 10); last.next = tmp; last = tmp;
            while n > 9:
               n /= 10
               last.next = last = ListNode(n % 10)
               return first


