import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(pokemon_id):
    url = f"{BASE_URL}{pokemon_id}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Ошибка: {response.status_code}")
        return None

    data = response.json()

    # Извлекаем основные поля
    pokemon = {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "base_experience": data["base_experience"],
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
    }

    return pokemon

def get_all_pokemon_data():
    all_pokemon_data = []
    
    for i in range(1, 152):  # Поколение 1, 151 покемон
        pokemon_data = get_pokemon_data(i)
        if pokemon_data:
            all_pokemon_data.append(pokemon_data)
    
    return all_pokemon_data
