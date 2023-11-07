class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort(head):
    if not head or not head.next:
        return head
    
    mid = find_middle(head)
    left_half = head
    right_half = mid.next
    mid.next = None
    
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    sorted_list = merge(left_sorted, right_sorted)
    
    return sorted_list

def find_middle(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    dummy = ListNode(-1)
    current = dummy
    
    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
    
    if left:
        current.next = left
    if right:
        current.next = right
    
    return dummy.next

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)

print("Original Linked List:")
print_list(head)

sorted_head = merge_sort(head)
print("Sorted Linked List:")
print_list(sorted_head)
