'''
Input : L1->L2,L3,...Ln-1 -> Ln
Output : L1->Ln->L2->Ln-1..
'''

def reorder_ll(self,head):
    if head == None:
        return head
    stack=[]
    temp=head
    while temp != None:
        stack.append(temp)
        temp=temp.next
    list=head
    fromHead=head
    fromStack=True
    while (fromStack and list!=stack[-1] or (not fromStack and list!=fromHead)):
        if fromStack:
            fromHead = fromHead.next
            list.next=stack.pop()
            fromStack=False
        else:
            list.next=fromHead
            fromStack=True
        list.next=fromHead
    list.next=None
    