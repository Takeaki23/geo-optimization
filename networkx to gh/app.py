from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import network as net

app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/createGraph",
    name = "Create Graph",
    inputs=[
        hs.HopsInteger("Number", "N", "Number of node", hs.HopsParamAccess.ITEM, default= 100),
        
        hs.HopsInteger("Seed", "S", "Seed for randomness", hs.HopsParamAccess.ITEM, default= 10),

    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)

    ]
)
def createGraph(number, seed):

    G = net.randomgrapgh(number, seed)

    nodes = net.getNodes(G)
    edges = net.getEdges(G) 

    return nodes, edges





if __name__== "__main__":
    app.run(debug=True)