from math import ceil
from operator import itemgetter

weapons = [
    {
    'name': 'Dagger',
    'cost': 8,
    'dmg': 4,
    'armor': 0
    },
    {
    'name': 'Shortsword',
    'cost': 10,
    'dmg': 5,
    'armor': 0
    },
    {
    'name': 'Warhammer',
    'cost': 25,
    'dmg': 6,
    'armor': 0
    },
    {
    'name': 'Longsword',
    'cost': 40,
    'dmg': 7,
    'armor': 0
    },
    {
    'name': 'Greataxe',
    'cost': 74,
    'dmg': 8,
    'armor': 0
    }
]

armors = [
    {
    'name': 'None',
    'cost': 0,
    'dmg': 0,
    'armor': 0
    },
    {
    'name': 'Leather',
    'cost': 13,
    'dmg': 0,
    'armor': 1
    },
    {
    'name': 'Chainmail',
    'cost': 31,
    'dmg': 0,
    'armor': 2
    },
    {
    'name': 'Splintmail',
    'cost': 53,
    'dmg': 0,
    'armor': 3
    },
    {
    'name': 'Bandedmail',
    'cost': 75,
    'dmg': 0,
    'armor': 4
    },
    {
    'name': 'Platemail',
    'cost': 102,
    'dmg': 0,
    'armor': 5
    }
]

rings = [
    {
    'name': 'None',
    'cost': 0,
    'dmg': 0,
    'armor': 0
    },
    {
    'name': 'Damage +1',
    'cost': 25,
    'dmg': 1,
    'armor': 0
    },
    {
    'name': 'Damage +2',
    'cost': 50,
    'dmg': 2,
    'armor': 0
    },
    {
    'name': 'Damage +3',
    'cost': 100,
    'dmg': 3,
    'armor': 0
    },
    {
    'name': 'Defense +1',
    'cost': 20,
    'dmg': 0,
    'armor': 1
    },
    {
    'name': 'Defense +2',
    'cost': 40,
    'dmg': 0,
    'armor': 2
    },
    {
    'name': 'Defense +3',
    'cost': 80,
    'dmg': 0,
    'armor': 3
    }
]

def who_wins(player1, player2):
    players = {
        1: {
            'hp': player1['hp'],
            'netdmg': max(1, player1['dmg'] - player2['armor'])
        },
        2: {
            'hp': player2['hp'],
            'netdmg': max(1, player2['dmg'] - player1['armor'])
        }
    }
    
    turn = 1
    while players[1]['hp'] > 0 and players[2]['hp'] > 0:
        if turn == 1: other_player = 2
        else: other_player = 1
        players[other_player]['hp'] -= players[turn]['netdmg']
        if players[other_player]['hp'] <= 0: return turn
        turn = other_player

def main():
    with open("Day21.txt") as f:
        lines = f.readlines()
    boss = {}
    boss['hp'] = int(lines[0].strip().split(": ")[1])
    boss['dmg'] = int(lines[1].strip().split(": ")[1])
    boss['armor'] = int(lines[2].strip().split(": ")[1])

    least_coin = max(map(itemgetter('cost'), weapons))
    least_coin += max(map(itemgetter('cost'), armors))
    least_coin += sum(sorted(map(itemgetter('cost'), rings))[-2:])

    most_coin = 0

    for weapon in weapons:
        for armor in armors:
            for ring1 in rings:
                for ring2 in rings:
                    if ring1 == ring2 and ring1['name'] != 'None': pass
                    equipment = [weapon, armor, ring1, ring2]
                    armor_pts = sum(map(itemgetter('armor'), equipment))
                    dmg_pts = sum(map(itemgetter('dmg'), equipment))
                    player = {'hp': 100, 'armor': armor_pts, 'dmg': dmg_pts}
                    coins = sum(map(itemgetter('cost'), equipment))
                    if coins < least_coin and who_wins(player, boss) == 1:
                        least_coin = coins
                    if coins > most_coin and who_wins(player, boss) == 2:
                        most_coin = coins

    print("Least coin:", least_coin)
    print("Most coin:", most_coin)

if __name__ == '__main__':
    main()