"""This module defines the Graph class."""

import random


class Graph:
    """This class defines a graph using an adjacency list and it has multiple
    methods in order to calculate the min cut of a graph.

    """

    def __init__(self, adjacency_list):
        """Initialize the Graph class using an adjacency list.

        :param adjacency_list: The adjacency list of a graph.
        :type adjacency_list: dict.
        :returns: None
        :rtype: None

        """

        self.adjacency_list = adjacency_list

    def calc_min_cut(self, N):
        """Calculate the min cut of the graph.

        :param N: How many times to calculate the min cut of the graph.
        :type N: int
        :returns: The found min cut of the graph after N repeated trials.
        :rtype: int

        """

        res = []
        for i in range(N):
            res.append(self.Kargers_algorithm())

        return min(res)

    def contract(self, adjacency_list, u, v):
        """Contract vertices u and v of the given adjacency list into one vertex.

        :param adjacency_list: The adjacency list of a graph.
        :type adjacency_list: dict
        :param u: The first vertex to contract.
        :type u: int
        :param v: The second vertex to contract.
        :type v: int
        :returns: The adjacency list of the graph.
        :rtype: dict

        """

        adjacency_list[u].extend(adjacency_list[v])
        del adjacency_list[v]

        # Replace all occurences of v in the adjacency list by u.
        for vertex, con_vertex in adjacency_list.items():
            adjacency_list[vertex] = [
                u if x == v else x for x in adjacency_list[vertex]]

        return adjacency_list

    def Kargers_algorithm(self):
        """Karger's algorithm to calculate the min cut of a graph.

        :returns: The found min cut of the graph.
        :rtype: int

        """

        # Deep copy the adjacency list of the graph in order to calculate the
        # contracted graph without modifying the original adjacency list.
        contracted_adjacency_list = {vertex: list(
            con_vertex) for vertex, con_vertex in self.adjacency_list.items()}

        while len(contracted_adjacency_list) > 2:
            u, v = self.pick_random_edge(contracted_adjacency_list)
            contracted_adjacency_list = self.contract(
                contracted_adjacency_list, u, v)
            contracted_adjacency_list = self.remove_selfloops_vertex(
                contracted_adjacency_list, u)

        return len(list(contracted_adjacency_list.values())[0])

    def pick_random_edge(self, adjacency_list):
        """Pick a random edge from the given adjacency list.

        :param adjacency_list: The adjacency list of a graph.
        :type adjacency_list: dict
        :returns: The two vertices u and v of the randomly chosen edge.
        :rtype: int

        """

        u = random.choice(list(adjacency_list))
        v = random.choice(adjacency_list[u])

        return u, v

    def remove_selfloops_vertex(self, adjacency_list, u):
        """Remove self-loops from vertex u in the given adjacency list.

        :param adjacency_list: The adjacency list of a graph.
        :type adjacency_list: dict
        :param u: The vertex to remove the self-loops from.
        :type u: int
        :returns: The adjacency list of the graph.
        :rtype: dict

        """

        adjacency_list[u] = list(filter(lambda x: x != u, adjacency_list[u]))

        return adjacency_list
