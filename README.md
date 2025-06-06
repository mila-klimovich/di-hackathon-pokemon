# PokéAnalyzer  - The Ultimate Pokémon Stats Analysis Tool!

## What is This?

Welcome to **Pokémon Data Analysis**! This project is all about diving deep into the magical world of Pokémon. I'm not just catching 'em all—oh no! I'm analyzing the heck out of them. With this tool, you can explore data on Pokémon stats, types, abilities, and much more!

### What Problem Does It Solve?

Have you ever wondered if Pikachu is really the strongest Pokémon, or what’s the deal with all those weird Pokémon abilities? Yeah, me too. That's why I built this tool! It's designed to fetch Pokémon data and run analysis on it, so you can figure out things like:

- Which Pokémon have the highest stats?
- What is the distribution of Pokémon abilities?
...and more! 

### Features

- **Data Retrieval**: Fetches Pokémon data from the PokeAPI and a PostgreSQL database. 
- **Data Analysis**: Does cool queries like comparing Pokémon abilities, stats, and types.
- **Visualizations**: Makes things pretty with scatter plots, bar charts, and tables.

## How to Run It (on someone else’s computer)

Here's how to get Pokémon data and start analyzing it, no sweat:

### 1. Clone the repo:

First, grab the project from GitHub! git clone this repo!

### 2. Set up a Virtual Environment:

python -m venv venv

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

### 3. Install Dependencies:

pip install -r requirements.txt

### 4. Set Up PostgreSQL (the behind-the-scenes magic):

Make sure you’ve got PostgreSQL installed and running.
Create a database named pokemon (or use an existing one if you’re feeling lucky).
Add tables and insert data. 

### 5. Run the Project:
Now, for the fun part—running the project!

Option 1: Jupyter Notebook (easier and fancier):
To open the Jupyter Notebook and run the cells:

jupyter notebook

Option 2: Main File (just for fun, not as fancy):
The main.py file is there for demonstration purposes only. 
It’s not doing much except calling get_all_pokemon_data() to show the process in action:

python main.py

NOTE: If you’re looking for flashy visualizations, stick with the notebook. 
If you just want to see the data printing out in the terminal, main.py will do.

### 6. Enjoy the Pokémon Data (or at least pretend to be a Pokémon master):
Once you're up and running, you can now analyze all the Pokémon stats, abilities, and other good stuff. 
Prepare yourself for some epic insights and probably some questionable conclusions!