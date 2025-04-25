import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(pokemon_name):
    url = f"{BASE_URL}{pokemon_name.lower()}"
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
