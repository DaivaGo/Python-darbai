import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()

# Sukurkite lentelę knygos su šiais stulpeliais:
#
# * id (sveikasis skaičius, pirminis raktas),
# * pavadinimas (tekstas),
# * autorius (tekstas),
# * isleidimo_metai (sveikasis skaičius),
# * puslapiu_skaicius (sveikasis skaičius).

# c.execute("""
#     CREATE TABLE books(
#     id INTEGER PRIMARY KEY,
#     book_title TEXT,
#     book_authors TEXT,
#     publishing_year INTEGER,
#     pages INTEGER,
#     FOREIGN KEY(books_id) REFERENCES books(id))
#     """)

# books_data = [
#     ('1', 'Drambliukas netelpa i zaidimu aikstele', 'Raimondas Jurgaitis', 2022, 24),
#     ('2', 'Otis eina i darzeli', 'Skaiste Dirgeliene', 2023,35),
#     ('3', 'Spalvu namelis','Renata Bee', 2021, 40)]


# c.executemany('INSERT INTO books VALUES (?,?,?,?,?)', books_data)

# conn.commit()
#
# result = c.fetchall()

# print(books)

# conn.close()

# 2. Į lentelę knygos įterpkite bent tris įrašus su knygų informacija.
# 3. Parašykite SQL užklausą, kuri išvestų visas knygas,
# išleistas po 2000 metų, ir surūšiuotų jas pagal išleidimo metus mažėjančia tvarka.

# c.execute("""SELECT book_title, publishing_year as after_2000 FROM books
#            WHERE publishing_year > 2000
#            ORDER BY publishing_year DESC """)
# results = c.fetchall()
# print(results)
# conn.commit()
# conn.close()

# 4.Atnaujinkite vienos iš įvestų knygų puslapių skaičių.

# c.execute(""" UPDATE books SET pages = 35 WHERE id = (SELECT id from books WHERE book_title = 'Otis eina i darzeli')
#     and pages = 100""")
#
# results = c.fetchall()
# # print(results)
# conn.commit()
# conn.close()

# 5. Sukurkite antrą lentelę skaitytojai su šiais stulpeliais:
# * id (sveikasis skaičius, pirminis raktas),
# * vardas (tekstas),
# * pavarde (tekstas),
# gimimo_metai (sveikasis skaičius).

# c.execute("""
#     CREATE TABLE readers(
#     id INTEGER PRIMARY KEY,
#     first_name TEXT,
#     last_name TEXT,
#     birth_year INTEGER,
#     FOREIGN KEY(id) REFERENCES readers(id))
#      """)

# readers_data=[
#     ('1', 'Jonas', 'Jonaitis', 1985),
#     ('2', 'Petras', 'Petraitis', 1990),
#     ('3', 'Paulina', 'Paulaite', 1998)
# ]
# c.executemany('INSERT INTO readers VALUES (?,?,?,?)', readers_data)
#
# conn.commit()
# result = c.fetchall()
# # print(result)
# conn.close()

# 6. Sukurkite trečią lentelę skaitytos_knygos su šiais stulpeliais:
#      * skaitytojo_id (sveikasis skaičius, nuoroda į skaitytojai.id),
#      * knygos_id (sveikasis skaičius, nuoroda į knygos.id),
#      * skaitymo_data (data).
#
# c.execute('''
#     CREATE TABLE books_read(
#     id INTEGER PRIMARY KEY,
#     book_id INTEGER,
#     read_date INTEGER,
#     FOREIGN KEY (id) REFERENCES (id))
#  ''')
#
# books_read_data=[
#     ('1', '1', 2022),
#     ('2', '2', 2021),
#     ('3', '3', 2023)
# ]
#
# c.executemany('INSERT INTO books_read VALUES (?,?,?)', books_read_data)
#
# conn.commit()
# result = c.fetchall()
# print(result)
# conn.close()

LIKE#suranda pagal tam tikra sablona(uzklausa)

SELECT * FROM actor
WHERE first_name LIKE 'P%'
# WHERE first_name LIKE 'P_______'

# -- SELECT * FROM customer
# -- WHERE email LIKE '%@sakilacustomer.org'
#
# -- DISTINCT #pasalina pasikartojancias reiksmes
#
# -- SELECT DISTINCT first_name FROM actor
# -- #pasalino visas eilutes su tais paciais vardais
#
# # -- UNION sujungia rezultatus is dvieju uzklausu ir pasalina pasikartojancius irasus
#
# -- SELECT first_name FROM actor
# -- UNION
# -- SELECT first_name FROM customer
#
#
#
# # # SUB uzklausos - leidzia vykdyti uzklausas uzklausos viduje
# # SELECT title, lenght from film
# # WHERE lenght >(
# #     SELECT AVG (lenght) FROM film
# # )
#
