class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        l = 1
        node2 = head
        node = head
        last = None
        middle = None

        while node.next:
            l += 1
            if not node.next.next:
                last = node.next
                break
            node = node.next

        k = k % l        
        if k == 0:
            return head

        kl = 0
        while node2:
            kl += 1
            if l - kl == k:
                middle = node2
                break
            node2 = node2.next

        new_head = node2.next  
        node2.next = None      
        last.next = head       
        return new_head
    

                
            
                


        


                
        

        