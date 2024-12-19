#Python program to print topological sorting of a DAG
from collections import defaultdict

#Class to represent a graph
class Graph:
	def __init__(self,vertices):
		self.graph = defaultdict(list) #dictionary containing adjacency List
		self.V = vertices #No. of vertices

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# A recursive function used by topologicalSort
	def topologicalSortUtil(self,v,visited,stack):

		# Mark the current node as visited.
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if not visited[i]:
				self.topologicalSortUtil(i,visited,stack)

		# Push current vertex to stack which stores result
		stack.insert(0,v)

	# The function to do Topological Sort. It uses recursive
	# topologicalSortUtil()
	def topologicalSort(self):
		# Mark all the vertices as not visited
		visited = [False]*self.V
		stack =[]

		# Call the recursive helper function to store Topological
		# Sort starting from all vertices one by one
		for i in range(self.V):
			if i in self.graph and not visited[i]:
				self.topologicalSortUtil(i,visited,stack)

		# Print contents of stack
		print (stack)

g= Graph(8)
g.addEdge(6,7);
g.addEdge(1,2);
g.addEdge(1,4);
g.addEdge(4,3);
g.addEdge(2,3);
g.addEdge(2,5);
g.addEdge(3,5);

print ("Following is a Topological Sort of the given graph")
g.topologicalSort()