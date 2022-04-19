from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import graph as g

app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/createNetwork",
    name = "Create Networkx",
    inputs=[
        hs.HopsPoint("Points", "P", "Points for nodes", hs.HopsParamAccess.LIST),
        hs.HopsCurve("Curves", "C", "Curves for edges", hs.HopsParamAccess.LIST),

    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)

    ]
)
def createNetworkx(points, curves):

    G = g.createGraph(points, curves)

    nodes = g.getNodes(G)
    edges = g.getEdges(G) 
    print(len(nodes))

    return nodes, edges





if __name__== "__main__":
    app.run(debug=True)