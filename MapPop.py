import random
import pprint




rows,cols = 20,20

arr = [[0 for x in range(rows)] for y in range(cols)]



def randonnuminit(arrs,nums):

    indexs=[]

    for x in range(nums):

        randx = random.randrange(0,cols-1,1)
        randy = random.randrange(0, rows - 1, 1)

        if [randx,randy] not in indexs:

            indexs.append([randx,randy])

            arrs[randx][randy]=cols-1

    return  indexs

randomindices = randonnuminit(arr,5)


def gennums(arr,listx,nextnum):



    localrandindices=[]


    for x in listx:

        currx = x[0]
        curry = x[1]

        #left
        try:
            if arr[currx+1][curry] ==0:
                if currx+1>=0 and curry >=0:
                    arr[currx+1][curry]=nextnum-1
                    localrandindices.append([currx+1,curry])
        except IndexError:
            pass

        # Right
        try:
            if arr[currx - 1][curry]==0:
                if currx - 1 >= 0 and curry >= 0:
                    arr[currx - 1][curry] = nextnum - 1
                    localrandindices.append([currx - 1,curry])
        except IndexError:
            pass

        # Top
        try:
            if arr[currx] [curry+1]==0:
                if currx  >= 0 and curry+1 >= 0:
                    arr[currx ][curry+1] = nextnum - 1
                    localrandindices.append([currx,curry+1] )
        except IndexError:
            pass

        # Bot
        try:
            if arr[currx][ curry-1] ==0:
                if currx  >= 0 and curry-1 >= 0:
                    arr[currx ][curry-1] = nextnum - 1
                    localrandindices.append([currx,curry-1])
        except IndexError:
            pass

        # topleft
        try:
            if arr[currx-1][curry - 1] == 0:
                if currx-1 >= 0 and curry - 1 >= 0:
                    arr[currx-1][curry - 1] = nextnum - 1
                    localrandindices.append([currx-1, curry - 1])
        except IndexError:
            pass

        # topright
        try:
            if arr[currx + 1][curry + 1] == 0:
                if currx + 1 >= 0 and curry + 1 >= 0:
                    arr[currx + 1][curry + 1] = nextnum - 1
                    localrandindices.append([currx + 1, curry + 1])
        except IndexError:
            pass

        # botright
        try:
            if arr[currx - 1][curry + 1] == 0:
                if currx - 1 >= 0 and curry + 1 >= 0:
                    arr[currx - 1][curry + 1] = nextnum - 1
                    localrandindices.append([currx - 1, curry + 1])
        except IndexError:
            pass

        # botleft
        try:
            if arr[currx + 1][curry - 1] == 0:
                if currx + 1 >= 0 and curry - 1 >= 0:
                    arr[currx + 1][curry - 1] = nextnum - 1
                    localrandindices.append([currx + 1, curry - 1])
        except IndexError:
            pass

    return localrandindices


#-----------------------------------

s1 = gennums(arr,randomindices,14)

s2 = gennums(arr,s1,13)

s3 = gennums(arr,s2,12)

s4 = gennums(arr,s3,11)

s5 = gennums(arr,s4,10)

s6 = gennums(arr,s5,9)

s7 = gennums(arr,s6,8)

s8 = gennums(arr,s7,7)

s9 = gennums(arr,s8,6)

s10 = gennums(arr,s9,5)

s11 = gennums(arr,s10,4)

s12 = gennums(arr,s11,3)

s13 = gennums(arr,s12,2)

s14 = gennums(arr,s13,1)



pprint.pprint("--------------")

pprint.pprint(arr)







import seaborn as sb
import matplotlib.pyplot as plt

heat_map = sb.heatmap(arr, cmap="Reds",annot=True)
sb.set(font_scale=0.1)
plt.show()



