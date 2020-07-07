import random
import json

class Randomizer:
    def __init__(self, guntype, weapon, perk, lethal, tactical):
        self.guntype = guntype
        self.weapon = weapon
        self.perk = perk
        self.lethal = lethal
        self.tactical = tactical

    def a_randomize(self):
        with open('gun_attachments.json') as w:
            weapons = json.load(w)
        with open('blocker.txt', 'r') as nm:
            barrel_no_muzzle = list(item for item in nm)
        
        # Get 5 randomized values of attachment types
        att_types = list(item for item in weapons[self.guntype][0][self.weapon][0])
        rand_att_types = random.sample(att_types, 5)

        # Get a random value for each attachment type and place it in a list
        rand_picks = list(random.choice(weapons[self.guntype][0][self.weapon][0][rand_att_types[item]]) for item in range(len(rand_att_types)))
        rand_picks[:] = [item for item in rand_picks if item != '']

        # Get values from each item that are not compatible with certain attachment type if present then recurse function
        is_barrel_no_muzzle = any(item in barrel_no_muzzle for item in rand_picks)
        is_muzzle_in_picks = any(item in rand_picks for item in weapons[self.guntype][0][self.weapon][0]['Muzzle'])
        if is_barrel_no_muzzle and is_muzzle_in_picks and True:
            return self.a_randomize()
        return '\n'.join(rand_picks)

    def p_randomize(self):
        with open('perks.json') as p:
            perks = json.load(p)
        perk_colors = list(color for color in perks[self.perk][0])
        rand_perk = random.choice(perks[self.perk][0][perk_colors[color]] for color in range(len(perk_colors)))
        return '\n'.join(rand_perk)

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