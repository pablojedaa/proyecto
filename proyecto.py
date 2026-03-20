#establecemos conexión con la base de datos del betis
import sqlite3
conexion = sqlite3.connect('betis.db')
cursor = conexion.cursor()
