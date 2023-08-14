class Graph:
  def __init__(self, V, E):
    self.V = V;
    self.E = E;
  def getAdjList(self):
   listOfEdges = self.E
    solution = [len(self.V)]
    ll = linkedlist.LinkedList();
    for i in range(len(self.V)):
      if i == 0:
        curr_vertex = self.V[i]
        ll.head = linkedlist.Node(curr_vertex)
        currNode = ll.head;
      elif i > 0:
        solution.append(ll);
        ll.head = linkedlist.Node(curr_vertex)
        ll = linkedlist.LinkedList();
        
      for j in range(len(listOfEdges)):
        if listOfEdges[j][0] == curr_vertex:
          if not ll.head == linkedlist.Node(curr_vertex):
            ll.head = linkedlist.Node(curr_vertex)
          else:
            if currNode == ll.head:
              ll.head.next = linkedlist.Node(listOfEdges[j][1])
              currNode = ll.head.next;
              #print(currNode.data)
            else:
              currNode.next = linkedlist.Node(listOfEdges[j][1]);
              currNode = currNode.next;
              #print(currNode.data)              
    return solution
  def getMatrix(self):
    return False;
