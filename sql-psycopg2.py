import psycopg2


# connect to "Chinook database"
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query1- select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query2- select name from "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query3- select "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query4- select all from the "Atist" where "ArtistId" is 51
cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# fetch the results(multiple)
# results = cursor.fetchall()

# fetch the result(single)
results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
