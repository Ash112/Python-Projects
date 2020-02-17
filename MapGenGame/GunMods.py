from enum import Enum

# Defines Enums for Gun Additions

# Bullet ammo Types
class BulletType(Enum):
    LightAmmo=1
    HeavyAmmo=2
    ShotGunAmmo=3
    SniperAmmo=4

# Scope Types for Guns
class ScopeClass(Enum):
    NoScope = 1
    Scope_1X = 2
    Scope_2X = 3
    Scope_3X = 4
    Scope_6X = 5
    Scope_10X = 6

# Extended Mags for Guns
class ExtentedMagClass(Enum):
    DefaultMag = 1
    MediumMag = 2
    LargeMag = 3

# Barrel Stabilizer for Guns
class BarrelStabilizer(Enum):
    Level_1_Stabilizer = 1
    Level_2_Stabilizer = 2
    Level_3_Stabilizer = 3

# Stocks for Guns
class Stock(Enum):
    Level_1_Stock = 1
    Level_2_Stock = 2
    Level_3_Stock = 3
