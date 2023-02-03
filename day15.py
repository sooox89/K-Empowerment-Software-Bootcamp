# code03-01

pokemons = list() # 빈 배열


def add_data(pokemon):
    pokemons.append(None)

    # pokemons[len(pokemons) - 1] = pokemon
    pokemons[-1] = pokemon


add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(pokemons)

