class Listnode():
    def __init__(self,x):
        self.val=x
        self.next=None

def getSum(head):
    if head is None:
        return 0
    return head.val+ getSum(head.next)

head=Listnode(1)
a1=Listnode(2)
a2=Listnode(3)
a3=Listnode(4)
head.next = a1
a1.next = a2
a2.next = a3
print(getSum(head))
