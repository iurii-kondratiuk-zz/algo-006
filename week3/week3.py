
import math
import random


class UndirectedGraph(object):
	def __init__(self, vertecies):
		self.vertecies = [[] for i in range(vertecies)]

	def vertecies_count(self):
		return len(self.vertecies)

	def add_edge(self, i, j):
		self.vertecies[i].append(j)

	def copy(self):
		graph = UndirectedGraph(0)
		for adj_vertecies in self.vertecies:
			graph.vertecies.append(adj_vertecies[:])
		return graph

	def merge_vertecies(self, i, j):
		i_adj = self.vertecies[i]

		k = 0
		while k < len(i_adj):
			if i_adj[k] == j:
				i_adj.pop(k)
				k -= 1
			k += 1

		for v in self.vertecies[j]:
			if (v != i):
				self.add_edge(i, v)

				v_adj = self.vertecies[v]
				k = 0
				l = len(v_adj)
				while k < l:
					if(v_adj[k] == j):
						v_adj[k] = i
						break
					k += 1

		self.vertecies[j] = self.vertecies[self.vertecies_count()-1]
		for v in self.vertecies[j]:
			v_adj = self.vertecies[v]
			k = 0
			while k < len(v_adj):
				if(v_adj[k] == (self.vertecies_count()-1)):
					v_adj[k] = j
					break
				k += 1
		self.vertecies.pop()


def _kergerMinCut(graph, seed):
	random.seed(seed)

	while graph.vertecies_count() > 2:
		i = random.randint(0, graph.vertecies_count()-1)
		j = random.choice(graph.vertecies[i])
		graph.merge_vertecies(i, j)

	return len(graph.vertecies[0])

def kargerMinCut(graph, N):
	kerger_min_cut = _kergerMinCut(graph.copy(), 0)

	for i in range(int(N)):
		temp_min_cut = _kergerMinCut(graph.copy(), i)
		print str(i) + ': ' + str(temp_min_cut)
		if temp_min_cut < kerger_min_cut: 
			kerger_min_cut = temp_min_cut

	print 'kerger min cut: ' + str(kerger_min_cut)

def main():
	with open('kargerMinCut.txt') as f:
		lines = [x.split('\t') for x in f]

	graph = UndirectedGraph(200)

	for line in lines:
		tail = int(line[0]) - 1
		for head in line[1:-1]:
			graph.add_edge(tail, int(head)-1)

	N = math.log(graph.vertecies_count())
	print(kargerMinCut(graph, N))

if __name__ == '__main__':
	main()