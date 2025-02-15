import sqlite3
import json
import re  # To extract numbers from strings

# Connect to SQLite database
conn = sqlite3.connect("cookbox.db")
cursor = conn.cursor()

# Create the `recipes` table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_name TEXT NOT NULL,
    dish_name_latin TEXT NOT NULL,
    category TEXT NOT NULL,
    country TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    ingredient_details TEXT NOT NULL,
    instructions TEXT NOT NULL,
    prep_time INTEGER NOT NULL,
    photo_path TEXT NOT NULL
)
""")

# Load JSON data
with open("recipes.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Load the JSON file into a Python dictionary

# Access the list of recipes using the "recipes" key
recipes = data["recipes"]

# Insert recipes into the table
for recipe in recipes:
    # Extract the numeric part of prep_time using a regular expression
    prep_time = re.search(r"\d+", recipe["prep_time"])  # Finds the first number
    prep_time = int(prep_time.group()) if prep_time else 0  # Convert to int, default to 0 if no number

    cursor.execute("""
    INSERT INTO recipes (
        dish_name, 
        dish_name_latin, 
        category, 
        country, 
        ingredients, 
        ingredient_details, 
        instructions, 
        prep_time, 
        photo_path
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        recipe["dish_name"],
        recipe["dish_name_latin"],
        recipe["category"],
        recipe["country"],
        recipe["ingredients"],
        recipe["ingredients_details"],  # Corrected field name
        recipe["instructions"],
        prep_time,  # Use the extracted numeric prep_time
        recipe.get("photo_path", "")  # Default to an empty string if photo_path is missing
    ))

# Commit changes and close the connection
conn.commit()
conn.close()



