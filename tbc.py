#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:56:44 2024

@author: ieiuser
"""

import random

class Character(object):
    def __init__(self, name = "", HP = 20, accuracy = 50, maxDamage = 5, armor = 1):
        super().__init__()
        self.name = name
        self.HP = HP
        self.accuracy = accuracy
        self.maxDamage = maxDamage
        self.armor = armor
        

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def hitPoints(self):
        return self.__HP

    @hitPoints.setter
    def hitPoints(self, value):
        value = self.testInt(value, 0, 10, 0)
        self.__HP = value

    def printStats(self):
        print(f"""
{self.name}
		HP: {self.HP}
		Accuracy: {self.HP}
		Max Damage: {self.maxDamage}
		Armor: {self.armor}
		""")
        
    def hit(self, enemy):
        if random.randint(1,100) < self.accuracy:
            print(f"{self.name} hits {enemy.name}...")
            damage = random.randint(1, self.maxDamage)
            print(f"for {damage} points of damage...")
            damage -= enemy.armor
            if damage < 0:
                damage = 0
            if enemy.armor > 0:
                print(f" but {enemy.name} has {enemy.armor} of armor ")
            enemy.HP -= damage
        else: 
            print(f"{self.name} does no damage to {enemy.name}")
                

    def testInt(self, value, min = 0, max = 100, default = 0):
		#takes in value, checks to see if int between min and max
        out = default
        if type(value) == int: 
            if value >= min:
                if value <= max:
                    out = value
                        
                        
                        
                else:
                    print("Too large")
                    
            else:
                
                print("Too small")
                
        else:
            
            print("Must be an int")
            
        return out
    
def punchyPunchy(hero, monster):
    keepGoing = True
    while keepGoing:
        hero.hit(monster)
        monster.hit(hero)
        
        print(f"""{hero.name}: {hero.HP}
              {monster.name}: {monster.HP}""")
              
        if hero.HP <= 0:
            print("The forest cries for its protector. You have lost and the trees have died.")
            keepGoing = False
        elif monster.HP <= 0:
            print("Congratulations, Tyrande the marklu. You have successfully defeated the monster. You have grown wise from the ways of battle.")
            keepGoing = False
        start = input("Press <ENTER> for next round")
        

def main():
    c = Character()
    c.name = "Marklu"
    c.printStats()  #can add c.whatever stat and set whatever name or stats you want for this particular character

if __name__ == "__main__":
    main()