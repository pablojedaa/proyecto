#establecemos conexión con la base de datos del betis
import sqlite3
conexion = sqlite3.connect('betis_final.db')
cursor = conexion.cursor()
#definimos el CRUD para la tabla manager
def crear_manager():
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
#definimos el CRUD para la tabla marca
def crear_marca():
    nombre = input("Nombre de la marca a crear: ")
    dinero = input("Dinero generado de la marca: ")
    conexion.commit()
    print("Marca creada.")
def seleccionar_marca():
    cursor.execute("SELECT * FROM Marca")
    marca = cursor.fetchall()
    print("\nLista de marca: ")
    for i in marca:
        print(i)
def actualizar_marca():
    id_marca = input("ID de la marca a actualizar:")
    nuevo_nombre_marca = input("Nuevo nombre de la marca: ")
    cursor.execute("UPDATE Marca SET nombre = ? WHERE id_marca = ?", (id_marca, nuevo_nombre_marca, ))
    conexion.commit()
    print("Marca actualizada.")
def eliminar_marca():
    id_marca = input("ID de la marca a eliminar: ")
    cursor.execute("DELETE FROM Marca WHERE id_marca = ?", (id_marca,))
    conexion.commit()
    print("Marca eliminada.")

#creamos el CRUD para la tabla jugador con relaciones con las tablas manager y marca.
def crear_jugador():
    nombre = input("Nombre del jugador a crear: ")
    edad = input("Edad del jugador a crear: ")
    id_manager = input("ID del mager para el jugador a crear: ")
    id_marca = input("ID de la marca que usará el jugador a crear: ")
    conexion.commit()
    print("Jugador creado.")
def seleccionar_jugador():
    cursor.execute("SELECT * FROM Jugador")
    jugador = cursor.fetchall()
    print("\nLista de jugadores: ")
    for i in jugador:
        print(i)
def actualizar_jugador():
    id_jugador = input("ID del jugador a actualizar:")
    nuevo_nombre_jugador = input("Nuevo nombre del jugador: ")
    nuevo_manager_jugador = input("Nuevo nombre del manager para nuevo jugador: ")
    nueva_marca_jugador = input("Nueva marca que usará el jugador: ")
    cursor.execute("UPDATE Jugador SET nombre = ? WHERE id_jugador = ?", (id_jugador, nuevo_nombre_jugador, nuevo_manager_jugador, nueva_marca_jugador, ))
    conexion.commit()
    print("Jugador actualizado.")
def eliminar_jugador():
    id_jugador = input("ID del jugador a eliminar: ")
    cursor.execute("DELETE FROM Jugador WHERE id_jugador = ?", (id_jugador,))
    conexion.commit()
    print("Jugador eliminado.")

def menu():
    while True:
        print("n\===MENU PRINCIPAL===")
        print("1. Crear manager")
        print("2. Ver manager")
        print("3. Actualizar manager")
        print("4. Eliminar manager")

        print("5. Añadir marca")
        print("6. Ver marca")
        print("7. Actualizar marca")
        print("8 ELiminar marca")

        print("9. Crear jugador")
        print("10. Ver jugador")
        print("11. Actualizar jugador")
        print("12. Eliminar jugador")

        print("\n0.Salir")

        opcion_listado=input("Selecciona una opción: ")

