from typing import Optional

from dclasses import LevelMod, Character
from enums import Job


def get_level_mod(level: int) -> Optional[LevelMod]:
    if level == 80:
        return LevelMod(340, 380, 3300, 3400)
    else:
        return None  # TODO lower levels


def get_main_attribute(c: Character) -> Optional[int]:
    if c.job in [Job.DRG, Job.MNK, Job.SAM]:
        return c.a.strength
    elif c.job in [Job.BRD, Job.NIN, Job.MCH, Job.DNC]:
        return c.a.dexterity
    elif c.job in [Job.PLD, Job.WAR, Job.DRK, Job.GNB]:
        return c.a.vitality
    elif c.job in [Job.BLM, Job.SMN, Job.RDM, Job.BLU]:
        return c.a.intelligence
    elif c.job in [Job.WHM, Job.SCH, Job.AST]:
        return c.a.mind
    else:
        return None
