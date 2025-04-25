# from api_connection import get_pokemon_data
from api_connection import get_all_pokemon_data

# pikachu = get_pokemon_data("pikachu")
# print(pikachu)

def main():
    data = get_all_pokemon_data()
    if data:
        for pokemon in data:
            print(f"ID: {pokemon['id']}, Name: {pokemon['name']}, Types: {pokemon['types']}")
    else:
        print("Нет данных о покемонах")

if __name__ == "__main__":
    main()