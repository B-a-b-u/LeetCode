# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1 , l2) :
        num1_str = ""
        num2_str = ""
        while(l1 != None):
            num1_str += str(l1.val);
            l1 = l1.next;
        while(l2 != None):
            num2_str += str(l2.val);
            l2 = l2.next;
        num1 = int(num1_str[::-1])
        num2 = int(num2_str[::-1])
        num3 = str(num1 + num2)[::-1];
        head = ListNode(int(num3[0]))
        temp = head
        for i in num3[1:]:
            next_node = ListNode(int(i))
            temp.next = next_node
            temp = temp.next
        return head