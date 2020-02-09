import GunClass
import random
import MapGen

GunNames=["Ages","Dragon","Omni","Angel","Eon","Plasma","Armor","Fallen","Scale","Ashen"
        ,"Fang","Scar","Atomic","Flame","Scarlet","Black","Fire","Shade","Blade","Firefight"
        ,"Shadow","Blaze","Galaxy","Storm","Burn","Hades","Steel","Chaos","Incendiary","Sworn"
        ,"Chrome","Jade","Tornadic","Claw","Jadeite","Void","Crimson","Light","Vortex","Crypt"
        ,"Oath","Wing","Draconic","Oblivion","Xeno"]

def randomNameGen():

    num = random.randrange(0,len(GunNames),1)

    return GunNames[num]


class Player:

    def __init__(Self,Name):

        Self.Name = Name

        Self.Health = 100

        Self.PlayerGun = GunClass.RanGun(randomNameGen())

        Self.P1_Pos = []

    def SetPos(Self,x,y):

        Self.P1_Pos = [x,y]


        return Self.P1_Pos

    def PlayerProps(Self):

        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

        print("Name                = " + str(Self.Name))

        print("Health              = " + str(Self.Health))

        print(Self.PlayerGun.GunProps())

