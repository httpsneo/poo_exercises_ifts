import sqlite3


def conexion():
    return sqlite3.connect('./Uso_de_Bases_de_Datos/empleados.sqlite3')


def crearTabla():
    BD = conexion()
    cursor = BD.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nro_legajo INTEGER NOT NULL UNIQUE,
            dni INTEGER NOT NULL UNIQUE,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            area TEXT NOT NULL
        );
    ''')


def insertarEmpleado():
    try:
        BD = conexion()
        cursor = BD.cursor()
        numero_legajo = int(input('Ingrese el numero de legajo: '))
        dni = int(input('Ingrese el numero de dni: '))
        nombre = input('Ingrese el nombre: ')
        apellido = input('Ingrese el apellido: ')
        area = input('Ingrese el area: ')
        cursor.execute('''INSERT INTO empleados (nro_legajo, dni, nombre, apellido, area) VALUES(?,?,?,?,?);''',
                       (numero_legajo, dni, nombre, apellido, area))
        BD.commit()
        print('Empleado insertado correctamente.')
    except sqlite3.IntegrityError as e:
        print('Error: El número de legajo o DNI ya existe.', e)
    except Exception as e:
        print('Error al insertar el empleado.', e)
    finally:
        BD.close()


def seleccionarEmpleadoPorDNI():
    try:
        BD = conexion()
        cursor = BD.cursor()
        dni = int(input("Ingrese el número de DNI: "))

        cursor.execute('SELECT * FROM empleados WHERE dni = ?', (dni,))
        empleado = cursor.fetchone()

        if empleado:
            print(f'Empleado encontrado: {empleado}')
        else:
            print('No se encontro un empleado con ese DNI.')
    except Exception as e:
        print('Error al seleccionar empleado.', e)
    finally:
        BD.close()


def seleccionarEmpleadosTodos():
    try:
        BD = conexion()
        cursor = BD.cursor()
        cursor.execute('Select * FROM empleados')
        empleados = cursor.fetchall()
        if empleados:
            for empleado in empleados:
                print(empleado)
        else:
            print('No hay empleados registrados.')
    except Exception as e:
        print('Error al seleccionar empleados.', e)
    finally:
        BD.close()


def modificarAreaEmpleado():
    try:
        BD = conexion()
        cursor = BD.cursor()
        nro_legajo = int(input('Ingrese el numero de legajo: '))
        area_nueva = input('Ingrese la nueva area: ')
        cursor.execute(
            'UPDATE empleados SET area = ? WHERE nro_legajo = ?', (area_nueva, nro_legajo))
        if cursor.rowcount > 0:
            BD.commit()
            print('Area modificada correctamente.')
        else:
            print('No se encontro un empleado con ese numero de legajo.')
    except Exception as e:
        print('Error al modificar el area del empleado.', e)
    finally:
        BD.close()


def eliminarEmpleado():
    try:
        BD = conexion()
        cursor = BD.cursor()
        nro_legajo = int(
            input('Ingrese el numero de legajo del empleado a eliminar: '))
        cursor.execute(
            'DELETE FROM empleados WHERE nro_legajo = ?', (nro_legajo,))
        if cursor.rowcount > 0:
            BD.commit()
            print('Empleado eliminado correctamente.')
        else:
            print('No se encontro el empleado con ese numero de legajo.')
    except Exception as e:
        print('Error al eliminar empleado.', e)
    finally:
        BD.close()


def interfaz():

    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Insertar un registro de empleado.")
        print("2. Seleccionar un registro de empleado a partir de su número de DNI.")
        print("3. Seleccionar todos los empleados.")
        print("4. Modificar el área de un empleado por su número de legajo.")
        print("5. Eliminar un empleado por su número de legajo.")
        print("6. Finalizar.")
        opcion = int(input('Selecciona una opcion: '))

        if opcion == 1:
            insertarEmpleado()
        elif opcion == 2:
            seleccionarEmpleadoPorDNI()
        elif opcion == 3:
            seleccionarEmpleadosTodos()
        elif opcion == 4:
            modificarAreaEmpleado()
        elif opcion == 5:
            eliminarEmpleado()
        elif opcion == 6:
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


crearTabla()
interfaz()
