from enum import Enum

class BulletType(Enum):
    LightAmmo=1
    HeavyAmmo=2
    ShotGunAmmo=3
    SniperAmmo=4

class ScopeClass(Enum):
    ScopeNone = 1
    Scope1X = 2
    Scope2X = 3

class ExtentedMagClass(Enum):
    DefaultMag = 1
    MedMag = 2
    LargeMag = 3

class BarrelStabilizer(Enum):
    Level1Stabilizer = 1
    Level2Stabilizer = 2
    Level3Stabilizer = 3

class Stock(Enum):
    Level1Stock = 1
    Level2Stock = 2
    Level3Stock = 3
