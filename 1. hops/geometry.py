#we import all the libraries that our functions need here too
import random as r
import rhino3dm as rg

def createPointsOnSurface(count, surface):

    PtsOnSurf = []
    for _ in range(count):

        random_u = r.uniform(0,1)
        random_v = r. uniform(0,1)

        pt_on_surface = rg.Surface.PointAt(surface, random_u, random_v)

        PtsOnSurf.append(pt_on_surface)

    return PtsOnSurf


