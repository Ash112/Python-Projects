import GunClass
import random

GunNames=["Ages","Dragon","Omni","Angel","Eon","Plasma","Armor","Fallen","Scale","Ashen"
        ,"Fang","Scar","Atomic","Flame","Scarlet","Black","Fire","Shade","Blade","Firefight"
        ,"Shadow","Blaze","Galaxy","Storm","Burn","Hades","Steel","Chaos","Incendiary","Sworn"
        ,"Chrome","Jade","Tornadic","Claw","Jadeite","Void","Crimson","Light","Vortex","Crypt"
        ,"Oath","Wing","Draconic","Oblivion","Xeno"]

def randomNameGen():

    num = random.randrange(0,len(GunNames),1)

    return GunNames[num]


RandomGun = GunClass.RanGun(randomNameGen())

print(RandomGun.GunProps())




