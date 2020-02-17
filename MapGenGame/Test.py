import PlayerClass
import MapGen
import time

#------------TEST-------------#

#RandomMap = MapGen.Map(1,1)

#print(RandomMap.Init_P1_Loc())
#print(RandomMap.Init_P2_Loc())

#print(RandomMap.PrintMap())

#print(RandomMap.P_Dist())

#for x in range(4):

    #if(RandomMap.PrintMap()!="SAME LOCATION"):
        #print((x))
        #print(RandomMap.MoveRight())
       # print(RandomMap.PrintMap())
        #print(RandomMap.P_Dist())
        #time.sleep(0.5)
        #print("\n"*1)

    #else:

        #break
#===================================
NewMap =MapGen.Map(6,6)

NewP1 = PlayerClass.Player("Aspro")

P1_Pos=NewMap.Init_P1_Loc()
P2_Pos=NewMap.Init_P2_Loc()

print(NewMap.PrintMap())
print(NewP1.SetPos(P1_Pos[0],P1_Pos[1]))

NewP1.PlayerGun.FireGun()
