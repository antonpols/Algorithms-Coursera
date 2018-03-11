from graph import Graph


with open('kargerMinCut.txt', 'r') as f:
    adjacency_list = {vertex: con_vertices for (vertex, *con_vertices) in
                      [[int(y) for y in x.strip().split('\t')] for x in
                       f.readlines()]}

graph = Graph(adjacency_list)
print("The min cut of the graph defined by the adjacency list in the "
      "file 'kargerMinCut.txt' is: {0}".format(graph.calc_min_cut(10**2)))
