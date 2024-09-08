# UŽDUOTIS 1 - Find the number of red, yellow & green occurrences.
# Funkcija kuri skaičiuoja raudonos, geltonos ir žalios spalvos pasikartojimus

def count_lights(file_path):
    red_count = 0
    yellow_count = 0
    green_count = 0

# Atidaro failą ir perskaito jį po eilutę
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            red, yellow, green, _, _ = line.strip().split(',')
            red_count += int(red)
            yellow_count += int(yellow)
            green_count += int(green)

    return red_count, yellow_count, green_count


# Kelias iki data.txt failo
file_path = 'C:/Users/mmind/OneDrive/Desktop/task/data.txt'

# Skaičiuoti spalvų pasikartojimus
red_count, yellow_count, green_count = count_lights(file_path)

# Rezultatas
print(f"Red count: {red_count}, Yellow count: {yellow_count}, Green count: {green_count}")

# UŽDUOTIS 2 - Find how long each colour was active for.
# Funkcija kuri skaičiuoja kiek laiko raudona, geltona ir žalia spalva buvo aktyvios


def lights_time(file_path):
    red_time = 0
    yellow_time = 0
    green_time = 0

# Atidaro failą ir perskaito jį po eilutę
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            red, yellow, green, time_active, _ = line.strip().split(',')
            time_active = int(time_active)

            if int(red) == 1:
                red_time += time_active
            elif int(yellow) == 1:
                yellow_time += time_active
            elif int(green) == 1:
                green_time += time_active

    return red_time, yellow_time, green_time


# Kelias iki data.txt failo
file_path = 'C:/Users/mmind/OneDrive/Desktop/task/data.txt'

# Surandami ir suskaičiuojami visi laikai kiekvienos spalvos
red_time, yellow_time, green_time = lights_time(file_path)

# Rezultatas
print(f"Red active: {red_time} sec., Yellow active: {yellow_time} sec., Green active: {green_time} sec.")

# UŽDUOTIS 3 - Find all times when Green was active (by time)
# Funkcija kuri naudojama surasti visus laikus, kai žalia spalva buvo aktyvi


def green_active(file_path):
    green_active_times = []

# Atidaro failą ir perskaito jį po eilutę
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            red, yellow, green, _, time = line.strip().split(',')

            if int(green) == 1:
                green_active_times.append(time)

    return green_active_times


# Kelias iki data.txt failo
file_path = 'C:/Users/mmind/OneDrive/Desktop/task/data.txt'

# Surandami visi laikai, kai žalia spalva buvo aktyvi
green_times = green_active(file_path)

# Rzultatas
print("Green light was active at these times:")
for time in green_times:
    print(time)

# UŽDUOTIS 4 - Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data
# Funkcija rasti Red-Yellow-Green-Yellow-Red pilnus ciklus


def count_cycles(file_path):
    cycle_count = 0
    current_state = None
    sequence = []

# Atidaro failą ir perskaito jį po eilutę
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            red, yellow, green, _, _ = line.strip().split(',')

# Identifikuoti dabartinę spalvą
            if int(red) == 1:
                current_state = 'R'
            elif int(yellow) == 1:
                current_state = 'Y'
            elif int(green) == 1:
                current_state = 'G'

# Pridėti spalvą į seką
            if current_state:
                sequence.append(current_state)

# Patikrinti ar yra pilnas Red-Yellow-Green-Yellow-Red ciklas
            if len(sequence) >= 5 and sequence[-5:] == ['R', 'Y', 'G', 'Y', 'R']:
                cycle_count += 1
                sequence = []

    return cycle_count


# Kelias iki data.txt failo
file_path = 'C:/Users/mmind/OneDrive/Desktop/task/data.txt'

# Skaičiuoti pilnus ciklus
complete_cycles = count_cycles(file_path)

# Rezultatas
print(f"Full cycles of Red-Yellow-Green-Yellow-Red: {complete_cycles}")

# 5 UŽDUOTIS - Find number of lines with mistakes (multiple colours active at the same time or no colours active)
# Funkcija surasti eilutes su klaidomis


def count_mistakes(file_path):
    mistake_count = 0

# Atidaro failą ir perskaito jį po eilutę
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            red, yellow, green, _, _ = line.strip().split(',')

# Konvertuoja į sveikus skaičius
            red = int(red)
            yellow = int(yellow)
            green = int(green)

# Skaičiuoja aktyvių spalvų skaičių
            active_colors = red + yellow + green

# Jeigu yra daugiau nei viena spalva aktyvi arba nėra nė viena aktyvi, fiksuojama klaida
            if active_colors != 1:
                mistake_count += 1

    return mistake_count


# Kelias iki data.txt failo
file_path = 'C:/Users/mmind/OneDrive/Desktop/task/data.txt'

# Skaičiuoti eilutes su klaidomis
mistake_lines = count_mistakes(file_path)

# Rezultatas
print(f"Mistakes found in data: {mistake_lines}")
