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


if __name__ == "__main__":
  kim = Node("kimone")
  cici = Node("cici")
  foreign = Node("foreignn")
  kitkat = Node("kitkatkait")
  mani = Node("imani")
  chocc = Node("chocc_lit")
  thicky = Node("thicky")
  jaidime = Node("jaidime")
  kim.next = cici
  cici.next = foreign;
  foreign.next = kitkat
  kitkat.next = mani
  mani.next = chocc;
  chocc.next = thicky
  thicky.next = jaidime
  list = LinkedList(kim)
  list.printList();
