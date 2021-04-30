from dataclasses import dataclass

from enums import Job


@dataclass
class Attributes:
    strength: int
    dexterity: int
    vitality: int
    intelligence: int
    mind: int

    critical_hit_rate: int
    determination: int
    direct_hit_rate: int

    attack_power: int

    magic_attack_potency: int

    tenacity: int


@dataclass
class Character:
    job: Job
    level: int
    weapon_damage: int
    a: Attributes


@dataclass
class LevelMod:
    MAIN: int
    SUB: int
    DIV: int
    HP: int
