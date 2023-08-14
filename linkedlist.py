class Node:

  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next


class LinkedList:

  def __init__(self, head=None):
    self.head = Node(head)

  def printList(self):
    curr = self.head
    while (curr.next is not None):
      print(curr.data, end=" -> ")
      curr = curr.next

