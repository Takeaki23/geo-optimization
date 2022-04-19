from pyparsing import line_end, line_start
import rhino3dm as rg
import networkx as nx

GraphMatcher = nx.isomorphism.vf2userfunc.GraphMatcher


def createGraph(points, curves):

    G = nx.Graph()

    nodes = []
    for i in range(len(points)):
        G.add_node(i)

    for i in range(len(curves)):
        edge_start = line_start[i]
        edge_end = line_end[i]
        G.add_edge(edge_start, edge_end)

    return G


def getNodes(G):

    lay = nx.spiral_layout(G, scale=10)
    nodes = []
    for d in lay.values():
        pt = rg.Point3d( d[0], d[1] , 0)
        nodes.append(pt)

    return nodes


def getEdges(G):

    lay = nx.spiral_layout(G, scale=10)

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