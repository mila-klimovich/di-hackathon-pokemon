import pandas as pd
from api_connection import get_all_pokemon_data
from db_connection import get_db_connection

pokemon_data = get_all_pokemon_data()
df = pd.DataFrame(pokemon_data)

def insert_abilities(abilities):
    conn = get_db_connection()
    cur = conn.cursor()

    for ability in abilities:
        cur.execute(
            """
            INSERT INTO abilities (name)
            VALUES (%s)
            ON CONFLICT (name) DO NOTHING
            """,
            (ability,)
        )

    conn.commit()
    cur.close()

def insert_stats(stats):
    conn = get_db_connection()
    cur = conn.cursor()

    for stat in stats:
        cur.execute(
            """
            INSERT INTO stats (name)
            VALUES (%s)
            ON CONFLICT (name) DO NOTHING
            """,
            (stat,)
        )

    conn.commit()
    cur.close()

def insert_pokemon_abilities(pokemon_id, abilities):
    conn = get_db_connection()
    cur = conn.cursor()

    for ability in abilities:
        cur.execute(
            """
            INSERT INTO pokemon_abilities (pokemon_id, ability_id)
            SELECT %s, id FROM abilities WHERE name = %s
            ON CONFLICT (pokemon_id, ability_id) DO NOTHING
            """,
            (pokemon_id, ability)
        )

    conn.commit()
    cur.close()

def insert_pokemon_stats(pokemon_id, stats):
    conn = get_db_connection()
    cur = conn.cursor()

    for stat_name, base_stat in stats.items():
        cur.execute(
            """
            INSERT INTO pokemon_stats (pokemon_id, stat_id, value)
            SELECT %s, id, %s FROM stats WHERE name = %s
            ON CONFLICT (pokemon_id, stat_id) DO NOTHING
            """,
            (pokemon_id, base_stat, stat_name)
        )

    conn.commit()
    cur.close()

def insert_pokemon_data(df):
    conn = get_db_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(
            """
            INSERT INTO pokemons (id, name, height, weight)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
            """,
            (row["id"], row["name"], row["height"], row["weight"])
        )

        for t in row["types"]:
            cur.execute(
                """
                INSERT INTO pokemon_types (pokemon_id, type_id)
                SELECT %s, id FROM types WHERE name = %s
                ON CONFLICT (pokemon_id, type_id) DO NOTHING
                """,
                (row["id"], t)
            )

        insert_pokemon_abilities(row["id"], row["abilities"])

        insert_pokemon_stats(row["id"], row["stats"])

    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted successfully!")

if __name__ == "__main__":

    all_abilities = set()
    for ability_list in df["abilities"]:
        all_abilities.update(ability_list)

    all_stats = set()
    for stat_dict in df["stats"]:
        all_stats.update(stat_dict.keys())

    insert_abilities(all_abilities)
    insert_stats(all_stats)
    insert_pokemon_data(df)
