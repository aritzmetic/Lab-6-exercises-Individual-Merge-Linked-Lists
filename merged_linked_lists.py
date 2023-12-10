# Delera, Aritz b.

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def MergingTwoLists(list1, list2):
    partial_node = ListNode(0)
    current = partial_node

    while list1 and list2:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return partial_node.next

def printList(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage of this merged linked list
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

print("Input List 1:")
printList(list1)
print("Input List 2:")
printList(list2)

merged_list = MergingTwoLists(list1, list2)
print("Below is the Merged List of List 1 & List 2!")
print("Merged List:")
printList(merged_list)
