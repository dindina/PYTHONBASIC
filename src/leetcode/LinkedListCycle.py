from ListNode import ListNode
from typing import Optional 
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
            
        return False

sol = Solution()
head = ListNode.randomcyclelist()
#ListNode.print(head)
print(sol.hasCycle(head))


