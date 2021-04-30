import math
from decimal import Decimal
from typing import Optional

from dclasses import Character
from enums import Job
from helper import get_level_mod, get_main_attribute


def ap(c: Character) -> Optional[int]:
    ap = c.a.magic_attack_potency if c.job in [Job.WHM, Job.SCH, Job.AST, Job.BLM, Job.SMN, Job.RDM,
                                               Job.BLU] else c.a.attack_power
    if c.level == 80:
        # f(AP) = ⌊ 165 · ( AP - 340 ) / 340 ⌋ + 100
        return math.floor(165 * (ap - 340) / 340) + 100
    elif 50 < c.level < 80:
        # (AP) = ⌊ ( Level - 50 ) · 2.5 + 75 ⌋ · ( AP - LevelLv, MAIN) / LevelLv, MAIN⌋ + 100
        pass  # TODO lower levels
    elif 1 <= c.level <= 50:
        # f(AP) = ⌊ 75 · (AP - LevelLv, MAIN) / LevelLv, MAIN⌋ + 100
        pass  # TODO lower levels
    else:
        return None


def dmg(c: Character, potency: int) -> int:
    # Damage = ⌊ Potency · f(DET) · f(AP) ⌋ / 100 ⌋ / 1000 ⌋
    return math.floor(math.floor(math.floor(potency * det(c) * ap(c)) / 100) / 1000)


def det(c: Character) -> int:
    # f(DET) = ⌊ 130 · ( DET - LevelModLv, Main )/ LevelModLv, DIV + 1000 ⌋
    level_mod = get_level_mod(c.level)
    return math.floor(130 * (c.a.determination - level_mod.MAIN) / level_mod.DIV + 1000)


def tnc(c: Character) -> int:
    # f(TNC) = ⌊ 100 · ( TNC - LevelModLv, SUB )/ LevelModLv, DIV + 1000 ⌋
    level_mod = get_level_mod(c.level)
    return math.floor(100 * (c.a.tenacity - level_mod.SUB) / level_mod.DIV + 1000)


def wd(c: Character) -> int:
    # f(WD) = ⌊ (LevelModLv, MAIN · JobModJob, Attribute / 1000) + WD ⌋
    level_mod = get_level_mod(c.level)
    return math.floor((level_mod.MAIN * get_main_attribute(c) / 1000) + c.weapon_damage)


def crit(c: Character) -> int:
    # f(CRIT) = ⌊ 200 · (CRIT - LevelModLv, SUB) / LevelModLv, DIV + 1400 ⌋
    level_mod = get_level_mod(c.level)
    return math.floor(200 * (c.a.critical_hit_rate - level_mod.SUB) / level_mod.DIV + 1400)
