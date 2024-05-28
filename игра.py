p_name = 'Али'
p_hp = 100.0
p_lvl = 1
p_point = 0
p_damage = 0.0
p_inventory = ['Бита', 'Доширак']
p_wallet = {'Золотые монеты': 7, 'Серебрянные монеты': 21}

def print_info():
    print(f'{'-' * 60}\n' 
        f'Имя: {p_name} Здоровье: {p_hp}\n'
        f'Уровень: {p_lvl} Очки: {p_point}\n'
        f'Урон: {p_damage}\n'
        f'Инвентарь: {p_inventory}\n'
        f'Монеты: {p_wallet}\n'
        f'{'-' * 60}')

def create_npc(name: str, lvl: int, hp: float, damage: float, inventory: list, wallet: dict, friendly: bool, info = false):
    if info = True:
        print(f'{'-' * 60}\n'
              f'Имя: {name} Здоровье: {hp}\n'
              f'Уровень: {lvl} Очки: {point}\n'
              f'Урон: {damage}\n'
              f'Инвентарь: {inventory}\n'
              f'Монеты: {wallet}\n'
              f'{'-' * 60}')

    return name, lvl, hp, damage, inventory, wallet, friendly

npc_1 = create_npc('Маша', 2, 75.0, 5, ['Йойо'],
                   {'Золотые монеты': 4, 'Серебрянные монеты': 54}, True )
