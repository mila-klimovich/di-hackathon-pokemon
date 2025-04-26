from api_connection import get_all_pokemon_data  
def display_pokemon_data():
    data = get_all_pokemon_data()
    if data:
        for pokemon in data:
            print(f"ID: {pokemon['id']}, Name: {pokemon['name']}, Types: {pokemon['types']}")
    else:
        print("No data")


def main():
    print("Displaying Pokémon Data:")
    display_pokemon_data()


if __name__ == "__main__":
    main()
