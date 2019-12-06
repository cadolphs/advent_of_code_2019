import networkx as nx

class OrbitMap:

    def __init__(self, source='COM'):
        self.graph = nx.DiGraph()
        self.source = source
        self.num_orbits = {}

    def compute_lengths(self):
        self.num_orbits = nx.algorithms.single_source_dijkstra_path_length(self.graph, self.source)

    def add_orbit(self, center, orbiter):
        self.graph.add_edge(center, orbiter)

    def nodes(self):
        return self.graph.nodes()

    def count_orbits(self, node):
        if node not in self.num_orbits:
            self.compute_lengths()
        
        return self.num_orbits[node]

    def get_total_orbit_count(self):
        self.compute_lengths()

        return sum(self.num_orbits.values())

    def get_orbitee(self, node):
        predecessors = list(self.graph.predecessors(node))
        assert len(predecessors) == 1, "An object can't have more than 1 predecessor"
        return predecessors[0]

    def find_path_between(self, src, dest):
        return nx.algorithms.shortest_path(self.graph.to_undirected(), src, dest)

    def find_number_of_transfers(self, src, dest):
        orbitee_src = self.get_orbitee(src)
        orbitee_dest = self.get_orbitee(dest)

        transfer_path = self.find_path_between(orbitee_src, orbitee_dest)

        return len(transfer_path) - 1

    @classmethod
    def from_string(cls, input_str, source='COM'):
        orbit_map = cls(source=source)

        for orbit_line in input_str.split('\n'):
            center, orbiter = tuple(orbit_line.split(')'))
            orbit_map.add_orbit(center, orbiter)

        return orbit_map
