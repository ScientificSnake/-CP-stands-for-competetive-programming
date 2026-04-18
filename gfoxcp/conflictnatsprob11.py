class fighter:
    def __init__(self, hp, regen, attackcount,dmg,arm):
        self.maxhp = hp
        self.regen = regen
        self.attackcount = attackcount
        self.dmg = dmg
        self.arm = arm
        self.hp = self.maxhp
    
    def procregen(self):
        self.hp += self.regen
        self.hp = min(self.hp, self.maxhp)

    def damage_from(self, other):
        truedmg = other.dmg - self.arm
        truedmg = max(truedmg, 1)
        finaldmg = truedmg * other.attackcount
        self.hp -= finaldmg


nbattles = int(input())

for _ in range(nbattles):
    first, _, second = input().partition('vs')
    fighter1 = fighter(0,0,0,0,0)
    fighter2 = fighter(0,0,0,0,0)
    for index, fighterstr in enumerate([first, second]):
        fighterstr = fighterstr.rstrip()
        fighterstr = fighterstr.lstrip()
        fighterstr = fighterstr.lstrip('(')
        fighterstr = fighterstr.rstrip(')')
        
        stats = [float(x) for x in fighterstr.split('/')]
        if index ==  0:
            fighter1 = fighter(stats[0], stats[1], stats[2], stats[3], stats[4])
        else:
            fighter2 = fighter(stats[0], stats[1], stats[2], stats[3], stats[4])
    
    # fight!

    while True:
        # Regen phase
        for guy in [fighter1, fighter2]:
            guy : fighter
            guy.procregen()
        
        fighter1.damage_from(fighter2)
        fighter2.damage_from(fighter1)

        # check for round end

        if fighter1.hp <= 0 and fighter2.hp <= 0:
            print("Tie")
            break
        elif fighter1.hp <= 0 and fighter2.hp > 0:
            print("Fighter 2 wins")
            break
        elif fighter2.hp <= 0 and fighter1.hp > 0:
            print("Fighter 1 wins")
            break
        
