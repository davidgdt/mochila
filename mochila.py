import csv

class Pokemon:
    def __init__(self, name, weight, benefit):
        self.name = name
        self.weight = weight
        self.benefit = benefit
        self.ratio = benefit / weight

    def __lt__(self, other):
        return self.ratio < other.ratio

# Leer el archivo CSV y almacenar los datos en una lista
pokemons = []
with open("pokemon_data.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Saltar la fila de encabezados
    for row in csv_reader:
        try:
            name = row[0]  # Nombre del Pokemon
            weight = 1 / float(row[9])  # Usaremos la columna 'Generation' como probabilidad
            attack = int(row[4])
            defense = int(row[5])
            sp_atk = int(row[6])
            sp_def = int(row[7])
            speed = int(row[8])
            benefit = attack + defense + sp_atk + sp_def + speed
            pokemons.append(Pokemon(name, weight, benefit))
        except ValueError as e:
            print(f"Error en la fila {csv_reader.line_num}: {e}")

# Ordenar los Pokemon por su ratio de beneficio/peso
pokemons.sort(reverse=True)

# Seleccionar los 6 mejores Pokemon
best_pokemons = pokemons[:6]

# Obtener el máximo ratio de los 6 mejores Pokémon
max_ratio = max(pokemon.ratio for pokemon in best_pokemons)

# Imprimir los 6 mejores Pokemon
print("Los 6 mejores Pokemon para capturar son:")
for pokemon in best_pokemons:
    scaled_ratio = pokemon.ratio / max_ratio
    print(f"{pokemon.name} - Peso: {pokemon.weight:.2f}, Beneficio: {pokemon.benefit}, Media escalada: {scaled_ratio:.2f}")
