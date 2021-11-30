# A ride hailing company sometimes travels between cities.
# To avoid delays, a driver first checks for the shortest routes.
# Given a map of the cities and their bidirectional roads represented by a graph of nodes and edges.
# Determine the paths from the first node to the last node and choose the shortest length.
# Now select all paths that are that length. These are the shortest paths.
#  Return an array of strings, one for each road in order, where the value is
# YES if the road is along a shortest path and NO if it is not.
# The roads or edges are named using their 1-based index in the input arrays.


def classifyEdges(g_nodes, g_from, g_to, g_weight):
     # g_nodes: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     # g_from: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
     # g_to: [2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
     # g_weight: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     # 1. Find the shortest path from 1 to 10.
     # 2. Find all paths that are that length.
     # 3. Return an array of strings, one for each road in order, where the value is
     # YES if the road is along a shortest path and NO if it is not.
     # 4. The roads or edges are named using their 1-based index in the input arrays.
     # 5. Guaranteed constraints:
     # 1 ≤ k ≤ 10,
     # 10k - 1 ≤ n.
     # 6. [output] integer

     




