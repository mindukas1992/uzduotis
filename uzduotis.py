import pandas as pd

# Nurodytas kelias iki data.txt failo
file_path = 'C:/Users/mmind/OneDrive/Desktop/task/data.txt'

# Nuskaitytas data.txt failas naudojant pandas
df = pd.read_csv(file_path)

# UŽDUOTIS 1 - Find the number of red, yellow & green occurrences.

# Suskaičiuota kiekvienos šviesos pasikartojimų kiekis
red_count = df['Red'].sum()
yellow_count = df['Yellow'].sum()
green_count = df['Green'].sum()

print(f"Red count: {red_count}, Yellow count: {yellow_count}, Green count: {green_count}")
print('\n')

# UŽDUOTIS 2 - Find how long each colour was active for.

# Suskaičiuota kiekvienos šviesos aktyvumo laikas
red_time = df[df['Red'] == 1]['TimeActive'].sum()
yellow_time = df[df['Yellow'] == 1]['TimeActive'].sum()
green_time = df[df['Green'] == 1]['TimeActive'].sum()

print(f"Red active: {red_time} sec., Yellow active: {yellow_time} sec., Green active: {green_time} sec.")
print('\n')

# UŽDUOTIS 3 - Find all times when Green was active (by time)

# Išfiltruoti įrašai kada žalia šviesa buvo aktyvi
green_times = df.loc[df['Green'] == 1, 'Time']

print(f"Times when green was active:")
print('\n'.join(green_times))
print('\n')

# UŽDUOTIS 4 - Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data

# Sujungiami spalvų stulpeliai į vieną eilutę
df['state'] = df['Red'].astype(str) + df['Yellow'].astype(str) + df['Green'].astype(str)

# Sukurtas sąrašas su teisinga ciklo seka
correct_cycle = ['100', '010', '001', '010', '100']

# Dabartinė pozicija sekoje ir ciklų skaičius
current_position = 0
cycle_count = 0

# Iteruojama per visas eilutes
for state in df['state']:
    if state == correct_cycle[current_position]:
        current_position += 1
        if current_position == len(correct_cycle):
            cycle_count += 1
            current_position = 0
    else:
# Jei ciklas sutriko, pradedama nuo naujo
        if state == '100':
            current_position = 1
        else:
            current_position = 0

print(f"Full cycles of Red-Yellow-Green-Yellow-Red: {cycle_count}")
print('\n')

# 5 UŽDUOTIS - Find number of lines with mistakes (multiple colours active at the same time or no colours active)

# Patikrinama eilutės ar yra klaidų
mistake_count = (df[['Red', 'Yellow', 'Green']].sum(axis=1) != 1).sum()

print(f"Mistakes found in data: {mistake_count}")
