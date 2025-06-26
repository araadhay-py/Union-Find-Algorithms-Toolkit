from disjoint_set import DisjointSet

# Count connected components
def count_connected_components(n, edges):
    dsu = DisjointSet(n)
    for u, v in edges:
        dsu.union(u, v)
    return len(set(dsu.find(i) for i in range(n)))

# Detect cycle in undirected graph
def detect_cycle(n, edges):
    dsu = DisjointSet(n)
    for u, v in edges:
        if not dsu.union(u, v):
            return True
    return False

# Kruskal’s MST
def kruskal_mst(n, edges):
    dsu = DisjointSet(n)
    edges.sort(key=lambda x: x[2])  # sort by weight
    mst_weight = 0
    for u, v, wt in edges:
        if dsu.union(u, v):
            mst_weight += wt
    return mst_weight

# Example usage
if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (3, 4)]
    print("Connected Components:", count_connected_components(5, edges))

    cycle_edges = [(0, 1), (1, 2), (2, 0)]
    print("Cycle Detected:", detect_cycle(3, cycle_edges))

    mst_edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2)]
    print("MST Weight:", kruskal_mst(4, mst_edges))
