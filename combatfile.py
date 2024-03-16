#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 21:22:25 2024

@author: ieiuser
"""

import tbc

def main():
    hero = tbc.Character()
    hero.name = "hero"
    hero.HP = 35
    hero.accuracy = 70
    hero.maxDamage = 10
    hero.armor = 0

    monster = tbc.Character("monster", 50, 30, 5, 5)

    hero.printStats()
    monster.printStats()

    tbc.punchyPunchy(hero, monster)
    


if __name__ == "__main__":
    main()
    