import math

from dclasses import Character
from helper import get_level_mod


def crit(c: Character) -> float:
    # p(CHR) = ⌊ 200 · ( CHR - LevelModLv, SUB )/ LevelModLv, DIV + 50 ⌋ / 10
    level_mod = get_level_mod(c.level)
    return math.floor(200 * (c.a.critical_hit_rate - level_mod.SUB) / level_mod.DIV + 50) / 10


def direct_hit(c: Character) -> float:
    # p(DHR) = ⌊ 550 · (DHR - LevelModLv, SUB) / LevelModLv, DIV ⌋ / 10
    level_mod = get_level_mod(c.level)
    return math.floor(550 * (c.a.direct_hit_rate - level_mod.SUB) / level_mod.DIV) / 10
