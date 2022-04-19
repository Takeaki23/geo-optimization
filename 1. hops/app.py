from flask import Flask
import ghhops_server as hs

#notice, we import another file as a library
import geometry as geo

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/PtsOnSurface",
    name = "Points on Surface",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of Points on Surface", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsSurface("Surface", "S", "Surface create points on", hs.HopsParamAccess.ITEM),

    ],
    outputs=[
       hs.HopsPoint("Points on Surface","PS","List of generated points on surface", hs.HopsParamAccess.LIST)
    ]
)
def PointsOnSurface(count, surface):

    randomPts = geo.createPointsOnSurface(count, surface)
    return randomPts



if __name__== "__main__":
    app.run(debug=True)