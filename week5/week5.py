class Graph:
	def __init__(self):
		self.edges = {}
		self.distances = {}
 
	def add_edge(self, from_node, to_node, distance):
		if not from_node in self.edges:
			self.edges[from_node] = []
		self.edges[from_node].append(to_node)
		self.distances[(from_node, to_node)] = distance

def _dijkstraSortestPaths(graph, sourceNode):
	visited = {sourceNode: 0}
	nodes = graph.edges.keys()

	while nodes: 
		min_node = None
		for node in nodes:
			if node in visited:
				if min_node is None:
					min_node = node
				elif visited[node] < visited[min_node]:
					min_node = node

		if min_node is None:
			break

		nodes.remove(min_node)
		current_weight = visited[min_node]

		for edge in graph.edges[min_node]:
			weight = current_weight + graph.distances[(min_node, edge)]
			if edge not in visited or weight < visited[edge]:
				visited[edge] = weight

	return visited

def dijkstraSortestPaths(graph, sourceNode, goal):
	shortest_paths = _dijkstraSortestPaths(graph, sourceNode)

	result = [shortest_paths[i] for i in goal]

	return result

def main():
	sourceNode = 1
	goal = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
	graph = Graph()

	with open('dijkstraData.txt') as f:
		for line in f:
			edges = line.strip().split()
			node = int(edges[0])
			for edge in edges[1:]:
				graph.add_edge(node, int(edge.split(',')[0]), int(edge.split(',')[1]))

	print dijkstraSortestPaths(graph, sourceNode, goal)

if __name__ == '__main__':
	main()