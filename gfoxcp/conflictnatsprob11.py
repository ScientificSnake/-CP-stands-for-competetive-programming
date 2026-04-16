class fighter:
    def __init__(self, hp, regen, attackcount,dmg,arm):
        self.hp = hp
        self.regen = regen
        self.attackcount = attackcount
        self.dmg = dmg
        self.arm = arm

nbattles = int(input())

for _ in range(nbattles):
    first, _, second = input().partition('vs')
    for index, fighterstr in enumerate([first, second]):
        fighterstr = fighterstr.rstrip()
        fighterstr = fighterstr.lstrip()
        fighterstr = fighterstr.lstrip('(')
        fighterstr = fighterstr.rstrip(')')

        


        stats = [int(x) for x in fighterstr.split('/')]
        if index ==  0:
            fighter1 = fighter(stats[0], stats[1], stats[2], stats[3], stats[4])
        else:
            fighter2 = fighter(stats[0], stats[1], stats[2], stats[3], stats[4])
    
    # fight!

    while True:
        # Regen phase
        for guy in [fighter1, fighter2]:

