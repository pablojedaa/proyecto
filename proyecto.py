#establecemos conexión con la base de datos del betis
import sqlite3
conexion = sqlite3.connect('betis.db')
cursor = conexion.cursor()
#definimos el CRUD para la tabla manager
def crear_manager():
    id_manager = input("ID del manager a crear: ")
    nombre = input("Nombre del manager a crear: ")
    edad = input("Edad del manager a crear: ")
    conexion.commit()
    print("Manager creado.")
def seleccionar_manager():
    cursor.execute("SELECT * FROM Manager")
    manager = cursor.fetchall()
    print("\nLista de managers: ")
    for i in manager:
        print(i)
def actualizar_manager():
    id_manager = input("ID del manager a actualizar:")
    nuevo_nombre_manager = input("Nuevo nombre del manager: ")
    cursor.execute("UPDATE Manager SET nombre = ? WHERE id_manager = ?", (id_manager, nuevo_nombre_manager, ))
    conexion.commit()
    print("Manager actualizado.")
def eliminar_manager():
    id_manager = input("ID del manager a eliminar: ")
    cursor.execute("DELETE FROM Manager WHERE id_manager = ?", (id_manager,))
    conexion.commit()
    print("Manager eliminado.")