import sys
import threading

t = 0
s = None
explored = None
scc_size = 0
finish_time = None

def _DFS_Loop_1(graph):
	global t, explored, finish_time

	t = 0
	n = len(graph)
	explored = [False] * n
	finish_time = [None] * n

	for i in reversed(range(n)):
		if not explored[i]:
			_DFS_1(graph, i)

def _DFS_1(graph, i):
	global t, explored
	
	explored[i] = True
	
	for v in graph[i]:
		if not explored[v]:
			_DFS_1(graph, v)

	finish_time[t] = i
	t += 1

def _DFS_Loop_2(graph):
	global scc_size, explored, finish_time

	n = len(graph)
	result = []	
	explored = [False] * n

	for i in reversed(range(n)):
		if not explored[finish_time[i]]:
			scc_size = 0
			_DFS_2(graph, finish_time[i])
			result.append(scc_size)

	return result

def _DFS_2(graph, i):
	global explored, scc_size

	explored[i] = True

	for v in graph[i]:
		if not explored[v]:
			_DFS_2(graph, v)

	scc_size += 1

def kosarajuSCCsizes(graph):
	_DFS_Loop_1(graph.vertecies_reversed)
	result = _DFS_Loop_2(graph.vertecies)

	return result

def createDirectedGraph(filename):
	f = open(filename)
	
	graph = []
	graph_rev = []
	
	line = f.readline()
	while line != '':
		edge = line.split()
		tail = int(edge[0])
		head = int(edge[1])
		max_vert = max(tail, head)

		while len(graph) < max_vert:
			graph.append([])
		while len(graph_rev) < max_vert:
			graph_rev.append([])
			
		graph[tail-1].append(head-1)
		graph_rev[head-1].append(tail-1)

		line = f.readline()

	return DirectedGraph(graph, graph_rev)

def main():
	graph = createDirectedGraph('SCC.txt')
	result = kosarajuSCCsizes(graph)

	print(','.join(map(lambda x: str(x), sorted(result)[::-1][:5])))


if __name__ == '__main__':
	threading.stack_size(67108864)
	sys.setrecursionlimit(2 ** 20)
	thread = threading.Thread(target = main)
	thread.start()