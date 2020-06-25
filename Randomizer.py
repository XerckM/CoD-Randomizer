import random
import json

class Randomizer:
    def __init__(self, weapon, perk, lethal, tactical): 
        self.weapon = weapon
        self.perk = perk
        self.lethal = lethal
        self.tactical = tactical

    def a_randomize(self):
        with open('gun_attachments.json') as w:
            weapons = json.load(w)
        with open('nomuzzle.txt', 'r') as nm:
            barrel_no_muzzle = list(i for i in nm)
        att_types = list(item for item in weapons[self.weapon][0])
        rand_att_types = random.sample(att_types, 5)
        first = random.choice(list(item for item in weapons[self.weapon][0][rand_att_types[0]]))
        second = random.choice(list(item for item in weapons[self.weapon][0][rand_att_types[1]]))
        third = random.choice(list(item for item in weapons[self.weapon][0][rand_att_types[2]]))
        fourth = random.choice(list(item for item in weapons[self.weapon][0][rand_att_types[3]]))
        fifth = random.choice(list(item for item in weapons[self.weapon][0][rand_att_types[4]]))
        rand_picks = [first, second, third, fourth, fifth]
        rand_picks[:] = [item for item in rand_picks if item != '']
        is_barrel_no_muzzle = any(item in barrel_no_muzzle for item in rand_picks)
        is_muzzle_in_picks = any(item in rand_picks for item in weapons[self.weapon][0]['Muzzle'])
        if is_barrel_no_muzzle is True:
            if is_muzzle_in_picks is True:
                return self.a_randomize()
        return '\n'.join(rand_picks)

    def p_randomize(self):
        with open('perks.json') as p:
            perks = json.load(p)
        first_perk = random.choice(list(perk for perk in perks[self.perk][0]['Blue']))
        second_perk = random.choice(list(perk for perk in perks[self.perk][0]['Red']))
        third_perk = random.choice(list(perk for perk in perks[self.perk][0]['Yellow']))
        return 'Blue Perk: ' + first_perk + '\n' + 'Red Perk: ' + second_perk + '\n' + 'Yellow Perk: ' + third_perk

    def l_randomize(self):
        with open('lethals.json') as l:
            lethals = json.load(l)
        rand_lethal = random.choice(list(lethal for lethal in lethals[self.lethal]))
        return rand_lethal
    
    def t_randomize(self):
        with open('tacticals.json') as t:
            tacticals = json.load(t)
        rand_tactical = random.choice(list(tactical for tactical in tacticals[self.tactical]))
        return rand_tactical