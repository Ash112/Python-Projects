import laspy
import numpy
import pptk

# read pointcloud file

pointcld = laspy.file.File("C:\\Users\\USER-PC\\Downloads\\TowerScan.las")

Xpoints = pointcld.x
Ypoints = pointcld.y
Zpoints = pointcld.z

# group into XYZ

datadim = numpy.vstack([Xpoints,Ypoints,Zpoints]).transpose()


# part of the data for testing

partdata = datadim[:1000]

# min and max data for all xyz

minz = min(Zpoints)
maxz = max(Zpoints)

minx = min(Xpoints)
maxx = max(Xpoints)

miny = min(Ypoints)
maxy = max(Ypoints)


# filter data aboev ground level
sepdata = []

for x in datadim:
    if(x[2]>=minz):

        sepdata.append(x)

proparray =numpy.asarray(sepdata)

banddata = []


# get a slice of data based on Z-Height
for z in proparray:

    if (z[2]>=83.000) and (z[2]<=89.010):


        banddata.append(z)


bandarray = numpy.asarray(banddata)



z = numpy.vstack(bandarray)

# normalized height for Color mapping
normalizedzval = []

for v in banddata:

    val = ((v[2]-minz)/(maxz-minz))

    normalizedzval.append(val)

zeros = numpy.zeros(bandarray.shape[0])


# create rgb values

rgb = numpy.array([normalizedzval,normalizedzval,normalizedzval]).transpose()

#----------------------------

# output in viewer

v = pptk.viewer(bandarray,rgb)
v.set(point_size=0.004)

print()