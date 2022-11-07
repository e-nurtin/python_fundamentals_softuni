def correct_values(numbers, factor):
    for number in range(len(numbers)):
        if numbers[number] <= factor:
            numbers[number] += factor
        else:
            numbers[number] -= factor
    return numbers


pokemons = list(map(int, input().split()))

total_pokemons = 0
command = int(input())
while len(pokemons) != 0:
    temporary_pokemon = 0

    if command < 0:
        temporary_pokemon = int(pokemons[0])
        pokemons[0] = pokemons[-1]

    elif command >= len(pokemons):
        temporary_pokemon = int(pokemons[-1])
        pokemons[-1] = pokemons[0]

    else:
        temporary_pokemon = pokemons.pop(command)

    pokemons = correct_values(pokemons, temporary_pokemon)
    total_pokemons += temporary_pokemon

    # if len(pokemons) == 0:
    #     break
    #
    command = int(input())

print(total_pokemons)
