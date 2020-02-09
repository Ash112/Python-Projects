import random
import math
import time

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

        if (Self.P1_Pos==Self.P2_Pos):

            return "SAME LOCATION"

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

        dist = ((Self.P2_Pos[0]-Self.P1_Pos[0])*(Self.P2_Pos[0]-Self.P1_Pos[0]))+((Self.P2_Pos[1]-Self.P1_Pos[1])*(Self.P2_Pos[1]-Self.P1_Pos[1]))

        return math.sqrt(dist)

    # Moves P1 1 unit to Right
    def MoveRight(Self):

        P2_Pos = Self.MoveRandomP2()
        # Gets Current Position of P1

        CurrentPosx = Self.P1_Pos[0]

        CurrentPosy = Self.P1_Pos[1]

        # Checks Edge Case Right

        if(CurrentPosy!=((Self.Mrows)-1)):

            # Sets Original Pos to 0 and Moves to Next

            Self.Arr[CurrentPosx][CurrentPosy] = 0

            Self.Arr[CurrentPosx][CurrentPosy+1] = 1

            Self.P1_Pos = [CurrentPosx, CurrentPosy+1]

            return "Moved P1 Right to " + str(Self.P1_Pos) ,P2_Pos

        else:

            return "Edge of Map Right" ,P2_Pos


    def MoveLeft(Self):

        P2_Pos = Self.MoveRandomP2()
        # Gets Current Position of P1

        CurrentPosx = Self.P1_Pos[0]

        CurrentPosy = Self.P1_Pos[1]

        # Checks Edge Case Left

        if(CurrentPosy!=0):

            # Sets Original Pos to 0 and Moves to Next

            Self.Arr[CurrentPosx][CurrentPosy] = 0

            Self.Arr[CurrentPosx][CurrentPosy-1] = 1

            Self.P1_Pos = [CurrentPosx, CurrentPosy-1]

            return "Moved P1 Left to " + str(Self.P1_Pos),P2_Pos

        else:

            return "Edge of Map Left",P2_Pos

    def MoveUp(Self):

        P2_Pos = Self.MoveRandomP2()
        # Gets Current Position of P1

        CurrentPosx = Self.P1_Pos[0]

        CurrentPosy = Self.P1_Pos[1]

        # Checks Edge Case Up

        if (CurrentPosx != 0):

            # Sets Original Pos to 0 and Moves to Next

            Self.Arr[CurrentPosx][CurrentPosy] = 0

            Self.Arr[CurrentPosx-1][CurrentPosy] = 1

            Self.P1_Pos = [CurrentPosx-1, CurrentPosy]

            return "Moved P1 Up to " + str(Self.P1_Pos),P2_Pos

        else:

            return "Edge of Map Up",P2_Pos

    def MoveDown(Self):

        P2_Pos=Self.MoveRandomP2()

        # Gets Current Position of P1

        CurrentPosx = Self.P1_Pos[0]

        CurrentPosy = Self.P1_Pos[1]

        # Checks Edge Case Up

        if (CurrentPosx != ((Self.Mrows)-1)):

            # Sets Original Pos to 0 and Moves to Next

            Self.Arr[CurrentPosx][CurrentPosy] = 0

            Self.Arr[CurrentPosx + 1][CurrentPosy] = 1

            Self.P1_Pos = [CurrentPosx + 1, CurrentPosy]

            return "Moved P1 Down to " + str(Self.P1_Pos),P2_Pos

        else:

            return "Edge of Map Down",P2_Pos

        # random Movement for P2

    def MoveRandomP2(Self):

        CurrentPosx = Self.P2_Pos[0]

        CurrentPosy = Self.P2_Pos[1]

        RandDir = random.randrange(1,4,1)

        # Move Right
        if(RandDir==1):

            if (CurrentPosy != ((Self.Mrows) - 1)):

                # Sets Original Pos to 0 and Moves to Next

                Self.Arr[CurrentPosx][CurrentPosy] = 0

                Self.Arr[CurrentPosx][CurrentPosy + 1] = 2

                Self.P2_Pos = [CurrentPosx, CurrentPosy + 1]

                return "P2 Moved Right " + str(Self.P2_Pos)

            else:

                return "No Right Movement P2"

        # Move Left
        if (RandDir == 2):

            if (CurrentPosy != 0):

                # Sets Original Pos to 0 and Moves to Next

                Self.Arr[CurrentPosx][CurrentPosy] = 0

                Self.Arr[CurrentPosx][CurrentPosy - 1] = 2

                Self.P2_Pos = [CurrentPosx, CurrentPosy - 1]

                return "P2 Moved Left " + str(Self.P2_Pos)

            else:

                return "No Left Movement P2"

        # Move Up
        if (RandDir == 3):

            if (CurrentPosx != 0):

                # Sets Original Pos to 0 and Moves to Next

                Self.Arr[CurrentPosx][CurrentPosy] = 0

                Self.Arr[CurrentPosx-1][CurrentPosy] = 2

                Self.P2_Pos = [CurrentPosx-1, CurrentPosy]

                return "P2 Moved Up " + str(Self.P2_Pos)

            else:

                return "No Up Movement P2"

        # Move Down
        if (RandDir == 4):

            if (CurrentPosx != ((Self.Mrows)-1)):

                # Sets Original Pos to 0 and Moves to Next

                Self.Arr[CurrentPosx][CurrentPosy] = 0

                Self.Arr[CurrentPosx+1][CurrentPosy] = 2

                Self.P2_Pos = [CurrentPosx+1, CurrentPosy]

                return "P2 Moved Down " + str(Self.P2_Pos)

            else:

                return "No Down Movement P2"

