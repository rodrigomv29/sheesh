class Node:

  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next


class LinkedList:

  def __init__(self, head=None):
    self.head = head;

  def isEmpty(self):
    if self.head.data is None:
      return True;
    return False;
  def printList(self):
    curr = self.head
    while curr:
      print(curr.data, end=" -> ")
      curr = curr.next
    print("/")
