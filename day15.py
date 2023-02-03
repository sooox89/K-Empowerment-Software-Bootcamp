pokemons = list() # 빈 배열


def add_data(pokemon):
    pokemons.append(None)
    kLen = len(pokemons)
    pokemons[kLen - 1] = pokemon


add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(pokemons)

