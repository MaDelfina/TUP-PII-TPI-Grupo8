import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    codigo_ingresado = input("Ingrese el codigo del libro:")

    libro_encontrado = False

    for libro in libros:
        if libro['cod'] == codigo_ingresado:
            libro_encontrado = libro #almacenamos el diccionario del libro encontrado en la variable libro_encontrado
            break #rompe el bucle

    if libro_encontrado is False:
        print("El codigo no existe.")
    else:
        print(f"Autor: {libro_encontrado['autor']}")
        print(f"Titulo: {libro_encontrado['titulo']}")
        print(f"Ejemplares disponibles: {libro_encontrado['cant_ej_ad']}")

        if libro_encontrado['cant_ej_ad'] == 0:
            print("No quedan ejemplares para prestar.")
        else:
            confirmacion = input("¿Desea confirmar el prestamo? (si/no): ")
            if confirmacion.lower() == "si":
                libro_encontrado['cant_ej_ad'] -= 1
                print("Prestamo confirmado.")
            else:
                print("Prestamo cancelado.")


def registrar_nuevo_libro(): #FALTA
    print()


def eliminar_ejemplar_libro():
    codigo_ingresado = input("Ingrese el codigo del libro para gestionar la devolucion:")

    libro_encontrado = False

    for libro in libros:
        if libro['cod'] == codigo_ingresado:
            if libro['cant_ej_ad'] > 0:
                libro['cant_ej_ad'] -= 1
                print("Ejemplar eliminado.")
                libro_encontrado = True
            else:
                print("No hay ejemplares.")
                libro_encontrado = True
    
    if libro_encontrado is False:
        print("El codigo no existe.")


def prestar_ejemplar_libro():
    for libro in libros:
        print(f"El libro es: {libro['titulo']}")
        if libro['cant_ej_pr'] > 0:
            print(f"Cantidad de ejemplares prestados: {libro['cant_ej_pr']}")
        else:
            print("No tiene ejemplares preatdos.")


def devolver_ejemplar_libro():
    codigo_ingresado = input("Ingrese el codigo del libro para gestionar la devolucion:")

    libro_encontrado = False

    for libro in libros:
        if libro['cod'] == codigo_ingresado:
            if libro['cant_ej_pr'] > 0:
                libro_encontrado = libro
            else:
                print("El libro no tiene ejemplares prestados.")

    if libro_encontrado is False:
        print("El codigo no existe.") #cuando el libro no tiene ejemplares nos salta este print tambien
    else:
        confirmacion = input("¿Quiere confirmar la devolucion? (si/no):")
        if confirmacion == "si":
            print("Confirmo la devolucion del libro.")
            libro_encontrado['cant_ej_ad'] += 1
        else:
            print("La confirmacion de su devolucion fue negada.")
            

def nuevo_libro():
    #completar
    return None