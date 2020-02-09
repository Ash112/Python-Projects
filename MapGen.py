import random
import math

class Map:

    def __init__(Self,cols,rows):

        Self.Mcols = cols

        Self.Mrows = rows

        Self.Arr = [[0 for x in range(rows)] for y in range(cols)]

        Self.P1_Pos = []

        Self.P2_Pos = []

    # prints th map in the current state
    def PrintMap(Self):

        for num in Self.Arr:

            print(num, sep="  ")

    def Init_P1_Loc(Self):

        randx_P1_pos = random.randrange(0,Self.Mrows,1)
        randy_P1_pos = random.randrange(0,Self.Mcols,1)

        Self.Arr[randx_P1_pos][randy_P1_pos] = 1

        Self.P1_Pos=[randx_P1_pos,randy_P1_pos]

        return Self.P1_Pos

    def Init_P2_Loc(Self):

        randx_P2_pos = random.randrange(0, Self.Mrows, 1)
        randy_P2_pos = random.randrange(0, Self.Mcols, 1)

        Self.Arr[randx_P2_pos][randy_P2_pos] = 2

        Self.P2_Pos = [randx_P2_pos, randy_P2_pos]

        return Self.P2_Pos

    def P_Dist(Self):

        dist = ((Self.P2_Pos[0]-Self.P1_Pos[0])*(Self.P2_Pos[0]-Self.P1_Pos[0]))
        +((Self.P2_Pos[1]-Self.P1_Pos[1])*(Self.P2_Pos[1]-Self.P1_Pos[1]))

        return math.sqrt(dist)




#----------------------------------

RandomMap = Map(6,6)

print(RandomMap.Init_P1_Loc())
print(RandomMap.Init_P2_Loc())

print(RandomMap.PrintMap())

print(RandomMap.P_Dist())