from db_connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    queries = [
'''
        CREATE TABLE IF NOT EXISTS pokemons (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            height FLOAT,
            weight FLOAT,
            generation INT
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS types (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS pokemon_types (
            pokemon_id INT REFERENCES pokemons(id) ON DELETE CASCADE,
            type_id INT REFERENCES types(id) ON DELETE CASCADE,
            PRIMARY KEY (pokemon_id, type_id)
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS abilities (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS pokemon_abilities (
            pokemon_id INT REFERENCES pokemons(id) ON DELETE CASCADE,
            ability_id INT REFERENCES abilities(id) ON DELETE CASCADE,
            PRIMARY KEY (pokemon_id, ability_id)
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS stats (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS pokemon_stats (
            pokemon_id INT REFERENCES pokemons(id) ON DELETE CASCADE,
            stat_id INT REFERENCES stats(id) ON DELETE CASCADE,
            value INT,
            PRIMARY KEY (pokemon_id, stat_id)
        );
        '''
    ]

    for query in queries:
        cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")