import random
import math

# Class for generating and traversing Map
class Map:

    def __init__(Self,cols,rows):

        Self.Mcols = cols

        Self.Mrows = rows

        Self.Arr = [[0 for x in range(rows)] for y in range(cols)]
        # Y is right ,Left Xis Up, Down
        Self.P1_Pos = []

        Self.P2_Pos = []

    # prints th map in the current state
    def PrintMap(Self):

        for num in Self.Arr:

            print(num, sep="  ")

    # Initializes P1 location randomly
    def Init_P1_Loc(Self):

        randx_P1_pos = random.randrange(0,Self.Mrows,1)
        randy_P1_pos = random.randrange(0,Self.Mcols,1)

        Self.Arr[randx_P1_pos][randy_P1_pos] = 1

        Self.P1_Pos=[randx_P1_pos,randy_P1_pos]

        return Self.P1_Pos

    # Initializes P2 location randomly
    def Init_P2_Loc(Self):

        randx_P2_pos = random.randrange(0, Self.Mrows, 1)
        randy_P2_pos = random.randrange(0, Self.Mcols, 1)

        Self.Arr[randx_P2_pos][randy_P2_pos] = 2

        Self.P2_Pos = [randx_P2_pos, randy_P2_pos]

        return Self.P2_Pos

    # Returns Distance between P2 & P2
    def P_Dist(Self):

        # Distance between Points Forumla

        dist = ((Self.P2_Pos[0]-Self.P1_Pos[0])*(Self.P2_Pos[0]-Self.P1_Pos[0]))
        +((Self.P2_Pos[1]-Self.P1_Pos[1])*(Self.P2_Pos[1]-Self.P1_Pos[1]))

        return math.sqrt(dist)

    # Moves P1 1 unit to Right
    def MoveRight(Self):

        # Gets Current Position of P1

        CurrentPosx = Self.P1_Pos[0]

        CurrentPosy = Self.P1_Pos[1]

        # Checks Edge Case Right

        if(CurrentPosy!=((Self.Mrows)-1)):

            # Sets Original Pos to 0 and Moves to Next

            Self.Arr[CurrentPosx][CurrentPosy] = 0

            Self.Arr[CurrentPosx][CurrentPosy+1] = 1

            Self.P1_Pos = [CurrentPosx, CurrentPosy+1]

            return "Moved P1 Right to " + str(Self.P1_Pos)

        else:

            return "Edge of Map Right"


    def MoveLeft(Self):

        # Gets Current Position of P1

        CurrentPosx = Self.P1_Pos[0]

        CurrentPosy = Self.P1_Pos[1]

        # Checks Edge Case Right

        if(CurrentPosy!=0):

            # Sets Original Pos to 0 and Moves to Next

            Self.Arr[CurrentPosx][CurrentPosy] = 0

            Self.Arr[CurrentPosx][CurrentPosy-1] = 1

            Self.P1_Pos = [CurrentPosx, CurrentPosy-1]

            return "Moved P1 Left to " + str(Self.P1_Pos)

        else:

            return "Edge of Map Left"






#----------------------------------

RandomMap = Map(6,6)

print(RandomMap.Init_P1_Loc())
print(RandomMap.Init_P2_Loc())

print(RandomMap.PrintMap())

print(RandomMap.P_Dist())



for x in range(5):
    
    print(RandomMap.MoveRight())

    print(RandomMap.PrintMap())