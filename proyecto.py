#establecemos conexión con la base de datos del betis

import sqlite3

#definimos el CRUD para la tabla manager

def crear_manager():
    try:
        conexion = sqlite3.connect('betis_final.db')
        cursor = conexion.cursor()
        nombre = input("Nombre del manager a crear: ")
        edad = input("Edad del manager a crear: ")
        cursor.execute("INSERT INTO Manager (nombre, edad) VALUES (?, ?)", (nombre, edad))
        conexion.commit()
        print(f"Manager '{nombre}' creado con éxito.")
    except sqlite3.DatabaseError:
        print("\nError, programa interrumpido")
    finally:
        conexion.close()       

def seleccionar_manager():
    try:
        conexion = sqlite3.connect('betis_final.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Manager")
        manager = cursor.fetchall()
        print("\nLista de managers: ")
        for i in manager:
            print(i)
    except sqlite3.DatabaseError:
        print("\nError, programa interrumpido")
    finally:
        conexion.close()    
    
def actualizar_manager():
    try:
        conexion = sqlite3.connect('betis_final.db')
        cursor = conexion.cursor()
        id_manager = input("ID del manager a actualizar: ")
        nuevo_nombre = input("Nuevo nombre del manager: ")
        cursor.execute("UPDATE Manager SET nombre = ? WHERE id_manager = ?", (nuevo_nombre, id_manager))
        conexion.commit()
        print(f"Manager ID {id_manager} actualizado a '{nuevo_nombre}'.")
    except sqlite3.DatabaseError:
        print("\nError, programa interrumpido")
    finally:
        conexion.close()    

def eliminar_manager():
    try:
        conexion = sqlite3.connect('betis_final.db')
        cursor = conexion.cursor()
        id_manager = input("ID del manager a eliminar: ")
        cursor.execute("DELETE FROM Manager WHERE id_manager = ?", (id_manager,))
        conexion.commit()
        print(f"Manager con ID {id_manager} eliminado de la base de datos.")
    except sqlite3.DatabaseError:
        print("\nError, programa interrumpido")
    finally:
        conexion.close()    

#definimos el CRUD para la tabla marca

def crear_marca():
    try:
        conexion = sqlite3.connect('betis_final.db')
        cursor = conexion.cursor()
        nombre = input("Nombre de la marca a crear: ")
        dinero = input("Dinero generado de la marca: ")
        cursor.execute("INSERT INTO Marca (nombre, dinero) VALUES (?, ?)", (nombre, dinero))
        conexion.commit()
        print(f"Marca '{nombre}' creada con éxito.")
    except sqlite3.DatabaseError:
        print("\nError, programa interrumpido")
    finally:
        conexion.close()    

def seleccionar_marca():
    try:
        conexion = sqlite3.connect('betis_final.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Marca")
        marca = cursor.fetchall()
        print("\nLista de marca: ")
        for i in marca:
            print(i)
    except sqlite3.DatabaseError:
        print("\nError, programa interrumpido")
    finally:
        conexion.close()    

def actualizar_marca():
    try:
        conexion = sqlite3.connect('betis_final.db')
        cursor = conexion.cursor()
        id_marca = input("ID de la marca a actualizar: ")
        nuevo_nombre = input("Nuevo nombre de la marca: ")
        cursor.execute("UPDATE Marca SET nombre = ? WHERE id_marca = ?", (nuevo_nombre, id_marca))
        conexion.commit()
        print(f"Marca ID {id_marca} actualizada a '{nuevo_nombre}'.")
    except sqlite3.DatabaseError:
        print("\nError, programa interrumpido")
    finally:
        conexion.close()    

def eliminar_marca():
    try:
        conexion = sqlite3.connect('betis_final.db')
        cursor = conexion.cursor()
        id_marca = input("ID de la marca a eliminar: ")
        cursor.execute("DELETE FROM Marca WHERE id_marca = ?", (id_marca,))
        conexion.commit()
        print(f"Marca con ID {id_marca} eliminada de la base de datos.")
    except sqlite3.DatabaseError:
        print("\nError, programa interrumpido")
    finally:
        conexion.close()    

#creamos el CRUD para la tabla jugador con relaciones con las tablas manager y marca.

def crear_jugador():
    try:
        conexion = sqlite3.connect('betis_final.db')
        cursor = conexion.cursor()
        nombre = input("Nombre del jugador a crear: ")
        edad = input("Edad del jugador a crear: ")
        id_manager = input("ID del manager para el jugador a crear: ")
        id_marca = input("ID de la marca que usará el jugador a crear: ")
        cursor.execute("INSERT INTO Jugadores (nombre, edad, id_manager, id_marca) VALUES (?, ?, ?, ?)", (nombre, edad, id_manager, id_marca))
        conexion.commit()
        print(f"Jugador '{nombre}' creado con éxito.")
    except sqlite3.DatabaseError:
        print("\nError, programa interrumpido")
    finally:
        conexion.close()    
    
def seleccionar_jugador():
    try:
        conexion = sqlite3.connect('betis_final.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Jugadores")
        jugador = cursor.fetchall()
        print("\nLista de jugadores: ")
        for i in jugador:
            print(i)
    except sqlite3.DatabaseError:
        print("\nError, programa interrumpido")
    finally:
        conexion.close()    

def actualizar_jugador():
    try:
        conexion = sqlite3.connect('betis_final.db')
        cursor = conexion.cursor()
        id_jugador = input("ID del jugador a actualizar: ")
        nuevo_nom = input("Nuevo nombre del jugador: ")
        nuevo_man = input("ID del nuevo manager: ")
        nueva_mar = input("ID de la nueva marca: ")
        cursor.execute("UPDATE Jugadores SET nombre = ?, id_manager = ?, id_marca = ? WHERE id_jugador = ?", (nuevo_nom, nuevo_man, nueva_mar, id_jugador))
        conexion.commit()
        print(f"Jugador ID {id_jugador} actualizado correctamente.")
    except sqlite3.DatabaseError:
        print("\nError, programa interrumpido")
    finally:
        conexion.close()    

def eliminar_jugador():
    try:
        conexion = sqlite3.connect('betis_final.db')
        cursor = conexion.cursor()
        id_jugador = input("ID del jugador a eliminar: ")
        cursor.execute("DELETE FROM Jugadores WHERE id_jugador = ?", (id_jugador,))
        conexion.commit()
        print(f"Jugador con ID {id_jugador} eliminado de la base de datos.")
    except sqlite3.DatabaseError:
        print("\nError, programa interrumpido")
    finally:
        conexion.close()    
        
def menu():
    while True:
        print("MENU PRINCIPAL")
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

#Creamos el main para que desde el menú nos lleve a la lista seleccionada según el valor siempre que este sea válido.

        if opcion_listado == "1":
            crear_manager()

        elif opcion_listado == "2":
            seleccionar_manager()

        elif opcion_listado == "3":
            actualizar_manager()

        elif opcion_listado == "4":
            eliminar_manager()

        elif opcion_listado == "5":
            crear_marca()

        elif opcion_listado == "6":
            seleccionar_marca()

        elif opcion_listado == "7":
            actualizar_marca()

        elif opcion_listado == "8":
            eliminar_marca()

        elif opcion_listado == "9":
            crear_jugador()

        elif opcion_listado == "10":
            seleccionar_jugador()

        elif opcion_listado == "11":
            actualizar_jugador()

        elif opcion_listado == "12":
            eliminar_jugador()

        elif opcion_listado == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intenta de nuevo")
        
#Añadimos, como se menciona anteriormente, y definimos el MAIN para el arranque y detenimiento de el menu

def main():
    menu()


if __name__ == "__main__":
    main()


