from random import randrange, randint

import functions as f
import math

import probabilities
from dclasses import Character, Attributes
from enums import Job


def main():
    attributes1 = Attributes(strength=309,
                             dexterity=340,
                             vitality=5145,
                             intelligence=357,
                             mind=5173,

                             critical_hit_rate=3352,
                             determination=2718,
                             direct_hit_rate=1220,

                             attack_power=309,

                             magic_attack_potency=5173,

                             tenacity=380)

    attributes2 = Attributes(strength=309,
                             dexterity=340,
                             vitality=5235,
                             intelligence=357,
                             mind=5245,

                             critical_hit_rate=3252,
                             determination=2891,
                             direct_hit_rate=1220,

                             attack_power=309,

                             magic_attack_potency=5173,

                             tenacity=380)

    character1 = Character(Job.SCH, 80, 174, attributes1)
    character2 = Character(Job.SCH, 80, 174, attributes2)

    potency = 290
    attacks = 100000

    # ----------------------------- #

    j = 0

    print(f"Calculating for {attacks} attacks...")
    while j < 5:
        total1 = 0
        total2 = 0
        i = 0

        while i < attacks:
            total1 += calc_damage(potency, character1)
            total2 += calc_damage(potency, character2)
            i += 1

        percentage = round((total2 / total1 - 1) * 100, 2)
        percentage = percentage if percentage < 0 else f"+{percentage}"
        print(f"Average 1: {total1 / attacks}")
        print(f"Average 2: {total2 / attacks} ({percentage}%)")
        j += 1


def calc_damage(potency: int, c: Character) -> int:
    d1 = math.floor(math.floor(math.floor(potency * f.dmg(c, potency) * f.det(c)) / 100) / 1000)
    d2 = math.floor(math.floor(math.floor(math.floor(
        math.floor(math.floor(d1 * f.tnc(c)) / 1000) * f.wd(c)) / 100) * 1) / 100)  # TODO replace 1 with trait

    p_val = randint(1, 100)
    crit = f.crit(c) if p_val <= probabilities.crit(c) else 1000
    dh = 125 if p_val <= probabilities.direct_hit(c) else 100
    d3 = math.floor(math.floor(math.floor(math.floor(d2 * crit) / 1000) * dh) / 100)

    return math.floor(math.floor(d3 * randint(95, 105)) / 100)  # TODO possibly add buffs


if __name__ == "__main__":
    main()
