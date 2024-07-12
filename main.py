# This Python script uses Dijkstra's Shortest Path algorithm for the traversal navigation of a moon rover that must
# collect core samples from 26 different locations. It will display each location it is currently at and report that
# the core sample was retrieved before moving to the next location.

from collections import defaultdict


class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Edges are bidirectional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


graph = Graph()
edges = [
    ('A', 'B', 3),
    ('A', 'C', 5),
    ('B', 'C', 3),
    ('B', 'D', 3),
    ('B', 'E', 3),
    ('C', 'D', 2),
    ('C', 'F', 2),
    ('E', 'G', 7),
    ('E', 'H', 2),
    ('F', 'G', 2),
    ('F', 'I', 4),
    ('G', 'I', 4),
    ('G', 'K', 4),
    ('G', 'L', 5),
    ('H', 'J', 5),
    ('H', 'K', 2),
    ('I', 'M', 3),
    ('I', 'N', 7),
    ('J', 'O', 4),
    ('J', 'P', 5),
    ('K', 'L', 1),
    ('K', 'O', 12),
    ('L', 'P', 6),
    ('L', 'R', 3),
    ('M', 'R', 8),
    ('M', 'U', 3),
    ('N', 'U', 2),
    ('N', 'V', 3),
    ('O', 'P', 4),
    ('O', 'Q', 10),
    ('P', 'Q', 2),
    ('Q', 'R', 2),
    ('Q', 'S', 4),
    ('R', 'S', 3),
    ('S', 'T', 2),
    ('S', 'W', 4),
    ('S', 'X', 6),
    ('T', 'U', 2),
    ('T', 'W', 2),
    ('U', 'W', 2),
    ('U', 'V', 2),
    ('V', 'W', 2),
    ('V', 'Y', 4),
    ('W', 'X', 3),
    ('X', 'Y', 1),
    ('X', 'Z', 6),
    ('Y', 'Z', 3),
]

for edge in edges:
    graph.add_edge(*edge)


    def navigate(graph, initial, end):
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()

        while current_node != end:
            # Call to the function or package traverse() goes here for the rover to mechanically traverse landscape
            visited.add(current_node)
            print("Arrived at location " + current_node)
            # Call to the function or package collectSample() goes here for the rover to mechanically collect a core sample
            print("Core sample retrieved.\n")
            locations = graph.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in locations:
                weight = graph.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

            next_locations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_locations:
                return "Route Not Possible"
            # Next location has the lowest destination node weight
            current_node = min(next_locations, key=lambda k: next_locations[k][1])

        # Works back through each destination in the shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        # Reverses the path
        path = path[::-1]
        print("\nShortest Path Between Start and End Locations: ", path)
        return path


navigate(graph, 'A', 'Z')
