# Populating Map with Terrain features #

import random
# used for Generating random initial indices
import pprint
import seaborn as sb
# for heat map Generation
import matplotlib.pyplot as plt



# define Rows Cols

rows,cols = 75,75

# create initial Array with "0"s with length rows,cols

arr = [[0 for x in range(rows)] for y in range(cols)]

# Def for generating nums at random indices for init
def randonnuminit(arrs,nums):

    indexs=[]

    for x in range(nums):



        randx = random.randrange(0,cols-1,1)
        randy = random.randrange(0, rows - 1, 1)

        if [randx,randy] not in indexs:

            randval = abs(random.randrange(round(cols/2), cols - 1, 1))

            indexs.append([randx,randy])

            arrs[randx][randy]=cols-1

    return  indexs

# Def for Generating Sloping values
def gennums(arr,listx):



    localrandindices=[]


    for x in listx:

        currx = x[0]
        curry = x[1]

        # Gets the curretn value of index in arr

        # calculates the new value , Should be >=0
        # for proper display in heat map

        newval = abs((arr[currx][curry])-1)


        # checking each cell from the original cell, used try to
        #avoid checking for edge case


        #left cell value(straight)
        try:
            # if cell is >0 then already occupied ,Ignore
            if arr[currx+1][curry] ==0:
                # minor edge case check
                if currx+1>=0 and curry >=0:
                    arr[currx+1][curry]=newval
                    # add new values indices to list for Next iteration
                    localrandindices.append([currx+1,curry])
        except IndexError:
            pass

        # Right cell value(straight)
        try:
            if arr[currx - 1][curry]==0:
                if currx - 1 >= 0 and curry >= 0:
                    arr[currx - 1][curry] = newval
                    localrandindices.append([currx - 1,curry])
        except IndexError:
            pass

        # Top cell value(straight)
        try:
            if arr[currx] [curry+1]==0:
                if currx  >= 0 and curry+1 >= 0:
                    arr[currx ][curry+1] = newval
                    localrandindices.append([currx,curry+1] )
        except IndexError:
            pass

        # Bot cell value(straight)
        try:
            if arr[currx][ curry-1] ==0:
                if currx  >= 0 and curry-1 >= 0:
                    arr[currx ][curry-1] = newval
                    localrandindices.append([currx,curry-1])
        except IndexError:
            pass

        # topleft cell value(diagonal)
        try:
            if arr[currx-1][curry - 1] == 0:
                if currx-1 >= 0 and curry - 1 >= 0:
                    arr[currx-1][curry - 1] = newval
                    localrandindices.append([currx-1, curry - 1])
        except IndexError:
            pass

        # topright cell value(diagonal)
        try:
            if arr[currx + 1][curry + 1] == 0:
                if currx + 1 >= 0 and curry + 1 >= 0:
                    arr[currx + 1][curry + 1] = newval
                    localrandindices.append([currx + 1, curry + 1])
        except IndexError:
            pass

        # botright cell value(diagonal)
        try:
            if arr[currx - 1][curry + 1] == 0:
                if currx - 1 >= 0 and curry + 1 >= 0:
                    arr[currx - 1][curry + 1] = newval
                    localrandindices.append([currx - 1, curry + 1])
        except IndexError:
            pass

        # botleft cell value(diagonal)
        try:
            if arr[currx + 1][curry - 1] == 0:
                if currx + 1 >= 0 and curry - 1 >= 0:
                    arr[currx + 1][curry - 1] = newval
                    localrandindices.append([currx + 1, curry - 1])
        except IndexError:
            pass

    return localrandindices


#-----------------------------------
# Calling random values for init once
randomindices = randonnuminit(arr,10)


s1 = gennums(arr,randomindices)

# looping n tmes to genrate terrain Nums
for x in range(cols-1):

    s2 = gennums(arr, s1)
    s1=s2
#------------------------------------

pprint.pprint("--------------")

pprint.pprint(arr)

# HeatMap using Seaborn
#heat_map = sb.heatmap(arr, cmap="Reds",annot=True)

heat_map = sb.heatmap(arr, cmap="Reds")
sb.set(font_scale=0.1)
plt.show()



