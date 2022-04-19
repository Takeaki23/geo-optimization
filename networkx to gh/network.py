from tkinter import Scale
import rhino3dm as rg
import networkx as nx
import random

GraphMatcher = nx.isomorphism.vf2userfunc.GraphMatcher


def randomgraph(number, seed):
        
    # Use seed when creating the graph for reproducibility
    G = nx.random_geometric_graph(number, radius=0.2, seed=seed)
    # # position is stored as node attribute data for random_geometric_graph
    # pos = nx.get_node_attributes(G, "pos")

    # # find node near center (0.5,0.5)
    # dmin = 1
    # ncenter = 0
    # for n in pos:
    #     x, y = pos[n]
    #     d = (x - 0.5) ** 2 + (y - 0.5) ** 2
    #     if d < dmin:
    #         ncenter = n
    #         dmin = d

    # # color by path length from node near center
    # p = dict(nx.single_source_shortest_path_length(G, ncenter))

    # nx.draw_networkx_edges(G, pos, alpha=0.4)
    # nx.draw_networkx_nodes(
    #     G,
    #     pos,
    #     nodelist=list(p.keys()),
    #     node_size=80,
    #     node_color=list(p.values()),
    # )
    return G


def getNodes(G):

    lay = nx.spectral_layout(G, scale = 10)

    nodes = []
    for d in lay.values():
        pt = rg.Point3d( d[0], d[1] , 0)
        nodes.append(pt)

    return nodes


def getEdges(G):

    lay = nx.spectral_layout(G, scale = 10)

    edges = []
    for e in G.edges:
        p1 = rg.Point3d( lay[e[0]][0], lay[e[0]][1], 0 )
        p2 = rg.Point3d( lay[e[1]][0], lay[e[1]][1], 0 )
        line = rg.LineCurve(p1, p2)
        edges.append(line)

    return edges


"""
G = createGridGraph(3,3)
GW = addRandomWeigrhs(G)

nodes = getNodes(G)
edges = getEdges(G)
"""


