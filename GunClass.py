from GunMods import *
from random import  *

# main Class Gun
class Gun:

    def __init__(Self, Name):

        Self.Name = ""

        Self.MaxAmmoCount = 0

        Self.CurrAmmoCount = 0

        Self.DamagePerBullet = 0

        Self.Accuracy = 0

        Self.Stability = 0

        Self.Bullet = BulletType

        Self.ScopeAttachment = ScopeClass

        Self.Magazine = ExtentedMagClass

        Self.BarrelStabilzer = BarrelStabilizer

        Self.GunStock = Stock


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

        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

        print("GunName             = " + str(Self.Name))

        print("BulletType          = " + str(Self.Bullet))

        print("Accuracy            = " + str(Self.Accuracy))

        print("Stability           = " + str(Self.Stability))

        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

        print("MaxAmmo             = " + str(Self.MaxAmmoCount))

        print("CurrAmmo            = " + str(Self.CurrAmmoCount))

        print("DamagePerBullet     = " + str(Self.DamagePerBullet))

        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

        print("ScopeAttachment     = " + str(Self.ScopeAttachment))

        print("Magazine            = " + str(Self.Magazine))

        print("BarrelStabilzer     = " + str(Self.BarrelStabilzer))

        print("GunStock            = " + str(Self.GunStock))

        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

# Random Gun Generator Class

class RanGun(Gun):

    def __init__(Self,Name):

        super().__init__(Name)

        Self.Name = Name

        Self.Bullet = BulletType(randrange(1,4,1))

        Self.ScopeAttachment = ScopeClass(randrange(1,3,1))

        Self.Magazine = ExtentedMagClass(randrange(1,3,1))

        Self.BarrelStabilzer = BarrelStabilizer(randrange(1,3,1))

        Self.GunStock = Stock(randrange(1,3,1))

        Self.Stability= (Self.ScopeAttachment.value+Self.Magazine.value\
                      +Self.BarrelStabilzer.value+Self.GunStock.value)

        #Ammo Damage,Capacity Types

        #Light Ammo

        if (Self.Bullet == BulletType(1)):

            Self.DamagePerBullet = 10

            Self.MaxAmmoCount = 30

            Self.CurrAmmoCount = 10

            Self.Accuracy = Self.Stability*0.50

            # Heavy Ammo

        elif (Self.Bullet == BulletType(2)):

            Self.DamagePerBullet = 25

            Self.MaxAmmoCount = 20

            Self.CurrAmmoCount = 10

            Self.Accuracy = Self.Stability * 0.75

            # ShotGun Ammo

        elif (Self.Bullet == BulletType(3)):

            Self.DamagePerBullet = 35

            Self.MaxAmmoCount = 10

            Self.CurrAmmoCount = 5

            Self.Accuracy = Self.Stability * 0.25

            # Sniper Ammo

        elif (Self.Bullet == BulletType(4)):

            Self.DamagePerBullet = 45

            Self.MaxAmmoCount = 5

            Self.CurrAmmoCount = 3

            Self.Accuracy = Self.Stability * 0.90



