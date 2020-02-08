from GunMods import *
from random import  *

# main Class Gun
class Gun:

    def __init__(Self, Name):

        Self.Name = ""

        Self.MaxAmmoCount = 0

        Self.CurrAmmoCount = 0

        Self.DamagePerBullet = 0

        Self.Bullet = BulletType

        Self.ScopeAttachment = ScopeClass

        Self.Magazine = ExtentedMagClass

        Self.BarrelStabilzer = BarrelStabilizer

        Self.GunStock = Stock

        #Light Ammo

        if(Self.Bullet==BulletType(1)):

            Self.DamagePerBullet = 10

            Self.MaxAmmoCount = 30

            Self.CurrAmmoCount = 10

        # Heavy Ammo

        elif(Self.Bullet==BulletType(2)):

            Self.DamagePerBullet = 25

            Self.MaxAmmoCount = 20

            Self.CurrAmmoCount = 10

        # ShotGun Ammo

        elif (Self.Bullet == BulletType(3)):

            Self.DamagePerBullet = 35

            Self.MaxAmmoCount = 10

            Self.CurrAmmoCount = 5

        # Sniper Ammo

        elif (Self.Bullet == BulletType(4)):

            Self.DamagePerBullet = 45

            Self.MaxAmmoCount = 5

            Self.CurrAmmoCount = 3


    def FireGun(Self):

        if (Self.CurrAmmoCount != 0):

            Self.CurrAmmoCount -= 1

        else:

            return "No Ammo"

    def ReloadGun(Self):

        if (Self.CurrAmmoCount != Self.MaxAmmoCount):

            Self.CurrAmmoCount = Self.MaxAmmoCount

        else:

            pass

    def GunProps(Self):

        print("GunName = "+str(Self.Name))

        print("MaxAmmo = "+str(Self.MaxAmmoCount))

        print("CurrAmmo = " + str(Self.CurrAmmoCount))

        print("BulletType = " + str(Self.Bullet))

        print("DamagePerBullet = " + str(Self.DamagePerBullet))

        print("ScopeAttachment = " + str(Self.ScopeAttachment))

        print("Magazine = " + str(Self.Magazine))

        print("BarrelStabilzer = " + str(Self.BarrelStabilzer))

        print("GunStock = " + str(Self.GunStock))

# Child Class Pistol

class Pistol(Gun):

    def __init__(Self, Name):
        super().__init__(Name)

        # Inherits from Gun Class

        Self.Name = Name

        Self.MaxAmmoCount = 15

        Self.CurrAmmoCount = 10

        Self.BulletType = "LightAmmo"

        Self.DamagePerBullet = 5

class RanGun(Gun):

    def __init__(Self,Name):

        super().__init__(Name)

        Self.Name = Name

        Self.Bullet = BulletType(randrange(1,4,1))

        Self.ScopeAttachment = ScopeClass(randrange(1,3,1))

        Self.Magazine = ExtentedMagClass(randrange(1,3,1))

        Self.BarrelStabilzer = BarrelStabilizer(randrange(1,3,1))

        Self.GunStock = Stock(randrange(1,3,1))