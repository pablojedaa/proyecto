#establecemos conexión con la base de datos del betis
import sqlite3
conexion = sqlite3.connect('betis.db')
cursor = conexion.cursor()
#insertamos los valores en la tabla manager
cursor.execute('''INSERT INTO Manager (id_manager, nombre, edad) VALUES(?,?,?)''', (1 ,"Pellegrini", 72))
cursor.execute('''INSERT INTO Manager (id_manager, nombre, edad) VALUES(?,?,?)''', (2 ,"Pepe Mel", 63))
cursor.execute('''INSERT INTO Manager (id_manager, nombre, edad) VALUES(?,?,?)''', (3 ,"Setién", 67))

#insertamos los valores en la tabla marca
cursor.execute('''INSERT INTO Marcas (id_marca, nombre, dinero) VALUES(?,?,?)''', (1 ,"Kappa", 36000000))
cursor.execute('''INSERT INTO Marcas (id_marca, nombre, dinero) VALUES(?,?,?)''', (2 ,"Adidas", 50000000))
cursor.execute('''INSERT INTO Marcas (id_marca, nombre, dinero) VALUES(?,?,?)''', (3 ,"Macron", 14000000))

#insertamos los valores en la tabla jugadores
cursor.execute('''INSERT INTO Marcas (id_jugador, nombre, edad, id_manager, id_marca) VALUES(?,?,?)''', (1 ,"Joaquín", 44, 1, 1))
cursor.execute('''INSERT INTO Marcas (id_jugador, nombre, edad, id_manager, id_marca) VALUES(?,?,?)''', (2 ,"Rubén Castro", 44, 2, 3))
cursor.execute('''INSERT INTO Marcas (id_jugador, nombre, edad, id_manager, id_marca) VALUES(?,?,?)''', (1 ,"Fabián", 29, 3, 2))
