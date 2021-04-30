from random import randrange, randint

import functions as f
import math

import probabilities
from dclasses import Character, Attributes
from enums import Job


def main():
    attributes1 = Attributes(309, 340, 5145, 357, 5173, 3352, 2718, 1220, 309, 5173, 380)
    character1 = Character(Job.SCH, 80, 174, attributes1)

    attributes2 = Attributes(309, 340, 5145, 357, 5173, 3352, 2718, 1220, 309, 5173, 380)
    character2 = Character(Job.SCH, 80, 174, attributes2)

    potency = 290
    attacks = 100000

    total1 = 0
    total2 = 0
    i = 0
    print(f"Calculating for {attacks} attacks...")
    while i < attacks:
        total1 += calc_damage(potency, character1)
        total2 += calc_damage(potency, character2)
        i += 1
    print(total1 / attacks)
    print(total2 / attacks)
    print(f"Second {round(total2 / total1, 4)}x damage of first")


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
