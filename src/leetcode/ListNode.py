# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def randomlist():
        head = ListNode(1)    
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        return head
    
    @staticmethod
    def randomcyclelist():
        head = ListNode(1)    
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = head
        return head
    
    @staticmethod
    def print(head):
        output = ""  # Initialize an empty string to build the output
        while head != None:
            output += str(head.val)
            if head.next:  # Add a separator if there's a next node
                output += " -> "
            head = head.next
        print(output) # Print the entire output string once at the end
