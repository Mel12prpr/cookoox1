import sqlite3


conn = sqlite3.connect("cookbox.db")
cursor = conn.cursor()
#
# cursor.execute("""
# UPDATE recipes
# SET prep_time = '45'
# WHERE prep_time like '45 minutes';
# """)

cursor.execute("""
UPDATE recipes 
SET ingredient_details = REPLACE(ingredient_details, 'ქათამი', 'ინდაური') 
WHERE dish_name = 'საცივი';
""")
conn.commit()
conn.close()