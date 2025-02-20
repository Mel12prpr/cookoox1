import sqlite3
import json
import re

conn = sqlite3.connect("cookbox.db")
cursor = conn.cursor()

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

# vxsniT json fails da mogvaqvs data
with open("recipes.json", "r", encoding="utf-8") as file:
    data = json.load(file)


recipes = data["recipes"]

# regexit ricxvis wamogeba
for recipe in recipes:
    prep_time = re.search(r"\d+", recipe["prep_time"])
    prep_time = int(prep_time.group()) if prep_time else 0

# jsonidan wamogebuli datas gashevba bazashi ufro martivad :)
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
        recipe["ingredients_details"],
        recipe["instructions"],
        prep_time,
        recipe.get("photo_path", "")
    ))

conn.commit()
conn.close()



