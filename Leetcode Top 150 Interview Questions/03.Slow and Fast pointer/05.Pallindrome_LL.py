#https://www.educative.io/courses/grokking-coding-interview-patterns-python/solution-palindrome-linked-list


def reverse_ll(slow):
    prev=None
    next=None
    curr=slow
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev

def compare_two_halves(first_half, sec_half):
    while first_half and sec_half:
        if first_half.data != sec_half.data:
            return False
        else:
            first_half=first_half.next
            sec_half=sec_half.next

    return True

def palindrome(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    revert_data = reverse_ll(slow)
    check=compare_two_halves(head, revert_data)

    reverse_ll(revert_data)

    if check:
        return True
    else:
        return False
    
