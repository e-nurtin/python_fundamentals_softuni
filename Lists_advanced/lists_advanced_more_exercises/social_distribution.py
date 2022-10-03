population_wealth = list(map(int, input().split(', ')))
minimum_wealth = int(input())

equality_possible = True
for index, number in enumerate(population_wealth):
    max_num_index = population_wealth.index(max(population_wealth))
    if number < minimum_wealth:
        diff = minimum_wealth - number
        population_wealth[index] += diff
        population_wealth[max_num_index] -= diff
        if population_wealth[max_num_index] < minimum_wealth:
            equality_possible = False

if not equality_possible:
    print("No equal distribution possible")
else:
    print(population_wealth)