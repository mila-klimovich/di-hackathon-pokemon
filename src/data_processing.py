import pandas as pd
from api_connection import get_all_pokemon_data

pokemon_data = get_all_pokemon_data()

df = pd.DataFrame(pokemon_data)

print(df.head())
