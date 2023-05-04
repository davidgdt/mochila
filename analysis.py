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
        name = row[0]  # Asumiendo que el nombre está en la primera columna
        weight = 1 / float(row[1])  # Asumiendo que la probabilidad está en la segunda columna
        attack = int(row[2])
        defense = int(row[3])
        others = int(row[4])
        benefit = attack + defense + others
        pokemons.append(Pokemon(name, weight, benefit))

# Ordenar la lista de Pokémon según su relación beneficio/peso
pokemons.sort(reverse=True)

# Imprimir los 6 mejores Pokémon
for i in range(6):
    print(f"{i+1}. {pokemons[i].name} (Ratio: {pokemons[i].ratio})")


