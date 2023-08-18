import linkedlist
from linkedlist import Node;
class Graph:
  adjacencyList = [];
  edgeMatrix = [];

  def __init__(self, V, E=[]):
    self.V = V
    self.E = E
  def isEdge(self, v1, v2):
    listOfEdges = self.E;
    for i in range(len(listOfEdges)):
      if listOfEdges[i][0] == v1:
        if listOfEdges[i][1] == v2:
          return True;
    
  def AdjList(self):
    listOfEdges = self.E
    solution = []
    ll = None
    for i in range(len(self.V)):
      curr_vertex = self.V[i]
      if i > 0 and not ll == None:
        solution.append(ll)
      ll = linkedlist.LinkedList()
      ll.head = Node(curr_vertex)
      currNode = ll.head
      for j in range(len(listOfEdges)):
        if listOfEdges[j][0] == curr_vertex:
          if currNode == ll.head:
            ll.head.next = Node(listOfEdges[j][1])
            currNode = ll.head.next
          else:
            currNode.next = Node(listOfEdges[j][1])
            currNode = currNode.next
    self.adjacencyList = solution;
    return self.adjacencyList;
  def matrixRepr(self):
    matrix = []
    #listOfEdges = self.E;
    for i in range(len(self.V)):
      matrix.insert(i, [])
      for j in range(len(self.V)):
        if self.isEdge(self.V[i], self.V[j]):
          matrix[i].append(1);
          continue;
        matrix[i].append(0)
    self.edgeMatrix = matrix
    return self.edgeMatrix;

  def printAdjList(self):
    for link in self.adjacencyList:
      link.printList();
if __name__ == "__main__":
  vertices = [1, 2, 3, 4, 5, 6]
  edges = [(1, 2), (1, 4), (2, 5), (3, 6), (3, 5), (4, 2), (5, 4), (6, 6)]
  g = Graph(vertices, edges)
  g.AdjList();
  g.matrixRepr()
  g.printAdjList();
