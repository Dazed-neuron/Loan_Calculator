initial_atoms = int(input())
final_atoms = int(input())

half_life = 12
half_life_periods = 0

while initial_atoms > final_atoms:

    initial_atoms = initial_atoms / 2

    half_life_periods += 1

print(half_life_periods * 12)