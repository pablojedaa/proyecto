#establecemos conexión con la base de datos del betis
import sqlite3
conexion = sqlite3.connect('betis.db')
cursor = conexion.cursor()
#insertamos los valores en la tabla manager
cursor.execute('''INSERT INTO Manager (id_manager, nombre, edad) VALUES(?,?,?)''', (1 ,"Pellegrini", 72))
cursor.execute('''INSERT INTO Manager (id_manager, nombre, edad) VALUES(?,?,?)''', (2 ,"Pepe Mel", 63))
cursor.execute('''INSERT INTO Manager (id_manager, nombre, edad) VALUES(?,?,?)''', (3 ,"Setién", 67))