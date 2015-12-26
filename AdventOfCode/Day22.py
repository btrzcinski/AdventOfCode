from operator import itemgetter
from time import sleep
from random import choice
from multiprocessing import Pool

spells = {
    'Poison':
    {
    'rank': 0,
    'name': 'Poison',
    'cost': 173,
    'dmg': 3,
    'hp': 0,
    'armor': 0,
    'mana': 0,
    'effect': 6
    },
    'Shield':
    {
    'rank': 1,
    'name': 'Shield',
    'cost': 113,
    'dmg': 0,
    'hp': 0,
    'armor': 7,
    'mana': 0,
    'effect': 6
    },
    'Recharge':
    {
    'rank': 2,
    'name': 'Recharge',
    'cost': 229,
    'dmg': 0,
    'hp': 0,
    'armor': 0,
    'mana': 101,
    'effect': 5
    },
    'Magic Missile':
    {
    'rank': 3,
    'name': 'Magic Missile',
    'cost': 53,
    'dmg': 4,
    'hp': 0,
    'armor': 0,
    'mana': 0,
    'effect': None # None = immediate effect
    },
    'Drain':
    {
    'rank': 4,
    'name': 'Drain',
    'cost': 73,
    'dmg': 2,
    'hp': 2,
    'armor': 0,
    'mana': 0,
    'effect': None
    }
}

debugging = False

def debug_print(debug_output):
    if debugging:
        print(debug_output)

# player_strategy = [spell, ...]
def who_wins(player, boss, player_strategy=[], hard_mode=False):
    player = player.copy()
    boss = boss.copy()
    player_strategy = [s.copy() for s in player_strategy]

    def reset_player():
        player['dmg'] = 0
        player['armor'] = 0
    reset_player()

    active_effects = []
    turn = 'Player'
    while True:
        debug_print("-- %s turn --" % turn)
        debug_print("- Player has %d hit points, %d armor, %d mana" % (player['hp'], player['armor'], player['mana']))
        debug_print("- Boss has %d hit points" % boss['hp'])

        # Take the turn
        move = None
        if turn == 'Player':
            try: move = player_strategy.pop(0)
            except:
                debug_print("Strategy exhausted; Boss wins.")
                return 'BossNoStrategy' # if you run out of strategy, you lose

        # Hard mode?
        if hard_mode and turn == 'Player':
            player['hp'] -= 1
            if player['hp'] <= 0: return 'Boss'

        # Apply effects
        for e in active_effects:
            player['dmg'] += e['dmg']
            player['armor'] += e['armor']
            player['mana'] += e['mana']
            player['hp'] += e['hp']
            e['effect'] -= 1
            debug_print("%s effect applied for %d dmg, %d armor, %d mana, %d hp, %d turns remaining" % (e['name'], e['dmg'], e['armor'], e['mana'], e['hp'], e['effect']))
        active_effects = [e for e in active_effects if e['effect'] > 0]
        
        if move is not None:
            player['mana'] -= move['cost']
            if player['mana'] < 0: return 'BossNoMana'
            # is this an effect? if so, it starts next time
            if move['effect'] is not None:
                if move['name'] in map(itemgetter('name'), active_effects):
                    return "BossInvalidSpell"
                debug_print("Player casts %s" % move['name'])
                active_effects.append(move.copy())
            # otherwise, apply it now
            else:
                debug_print("Player casts %s; dmg += %d, armor += %d, mana += %d, hp += %d" % (move['name'], move['dmg'], move['armor'], move['mana'], move['hp']))
                player['dmg'] += move['dmg']
                player['armor'] += move['armor']
                player['mana'] += move['mana']
                player['hp'] += move['hp']

        boss['hp'] -= player['dmg']
        debug_print("Player inflicts %d damage on boss" % player['dmg'])
        if boss['hp'] <= 0:
            debug_print("Boss hp is %d; Player wins" % boss['hp'])
            return 'Player'
        
        if turn == 'Boss':
            net_boss_damage = max(1, boss['dmg'] - player['armor'])
            debug_print("Boss inflicts %d damage on player" % net_boss_damage)
            player['hp'] -= net_boss_damage
            if player['hp'] <= 0:
                debug_print("Player hp is %d; Boss wins" % player['hp'])
                return 'Boss'

        reset_player()
        if turn == 'Player': turn = 'Boss'
        else: turn = 'Player'

def random_outcome(player, boss, hard_mode=False):
    spell_list = list(spells.values())
    strategy = [choice(spell_list)]
    outcome = who_wins(player, boss, strategy, hard_mode)
    while outcome == 'BossNoStrategy':
        strategy.append(choice(spell_list))
        outcome = who_wins(player, boss, strategy, hard_mode)
    return (outcome, sum(map(itemgetter('cost'), strategy)))

def least_mana_strategy_random_finder(player, boss, hard_mode=False, iterations=1000000):
    with Pool(8) as p:
        args = [(player, boss, hard_mode)] * iterations
        outcomes = p.starmap(random_outcome, args)
        outcomes = [o for o in outcomes if o[0] == 'Player']
        min_mana = min(map(itemgetter(1), outcomes))
    return min_mana

def main():
    with open("Day22.txt") as f:
        boss = {}
        boss['hp'] = int(f.readline().strip().split(" ")[-1])
        boss['dmg'] = int(f.readline().strip().split(" ")[-1])

    player = {'hp': 50, 'mana': 500}
    print("-- EASY MODE --")
    try:
        print(least_mana_strategy_random_finder(player, boss, False, 100000))
    except KeyboardInterrupt: pass
    print("-- HARD MODE --")
    try:
        print(least_mana_strategy_random_finder(player, boss, True, 100000))
    except KeyboardInterrupt: pass

if __name__ == '__main__':
    main()
