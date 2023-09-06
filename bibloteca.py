import libro as l #acceder a los objetos
import cod_generator

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    codigo_ingresado = input("Ingrese el codigo del libro: ")

    libro_encontrado = False

    for libro in libros:
        if libro['cod'] == codigo_ingresado:
            libro_encontrado = libro #almacenamos el diccionario del libro encontrado en la variable libro_encontrado
            break #rompe el bucle

    if libro_encontrado is False:
        print("El codigo no existe")
    else:
        print(f"Autor: {libro_encontrado['autor']}")
        print(f"Titulo: {libro_encontrado['titulo']}")
        print(f"Ejemplares disponibles: {libro_encontrado['cant_ej_ad']}")

        if libro_encontrado['cant_ej_ad'] == 0:
            print("No quedan ejemplares para prestar")
        else:
            confirmacion = input("¿Desea confirmar el prestamo? (si/no): ")
            if confirmacion.lower() == "si":
                libro_encontrado['cant_ej_ad'] -= 1
                print("Prestamo confirmado.")
            else:
                print("Prestamo cancelado")

def eliminar_ejemplar_libro():
    codigo_ingresado = input("Ingrese el codigo del libro para eliminar ejemplar: ")

    libro_encontrado = False

    for libro in libros:
        if libro['cod'] == codigo_ingresado:
            if libro['cant_ej_ad'] > 0:
                libro['cant_ej_ad'] -= 1
                print("Ejemplar eliminado")
                libro_encontrado = True
            else:
                print("No hay ejemplares")
                libro_encontrado = True
    
    if libro_encontrado is False:
        print("El codigo no existe")

def prestar_ejemplar_libro():
    for libro in libros:
        print(f"El libro es: {libro['titulo']}")
        if libro['cant_ej_pr'] > 0:
            print(f"Cantidad de ejemplares prestados: {libro['cant_ej_pr']}")
        else:
            print("No tiene ejemplares preatdos")

def devolver_ejemplar_libro():
    codigo_ingresado = input("Ingrese el codigo del libro para gestionar la devolucion: ")

    libro_encontrado = False

    for libro in libros:
        if libro['cod'] == codigo_ingresado:
            if libro['cant_ej_pr'] > 0:
                libro_encontrado = libro #almacenamos el diccionario del libro encontrado en la variable libro_encontrado
            else:
                print("El libro no tiene ejemplares prestados")

    if libro_encontrado is False:
        print("El codigo no existe") #cuando el libro no tiene ejemplares nos salta este print tambien
    else:
        confirmacion = input("¿Quiere confirmar la devolucion? (si/no): ")
        if confirmacion == "si":
            print("Confirmo la devolucion del libro")
            libro_encontrado['cant_ej_ad'] += 1
        else:
            print("La confirmacion de su devolucion fue negada")

def nuevo_libro():
    codigo_automatico = cod_generator.generar()
    cantidad_ej_ad = int(input("Ingrese la cantidad de ejemplares adquiridos: "))
    cantidad_ej_pr = int(input("Ingrese la cantidad de ejemplares prestados: "))
    titulo = str(input("Ingrese el titulo del libro: "))
    autor = str(input("Ingrese el autor: "))

    libro_nuevo = {'cod': codigo_automatico, 'cant_ej_ad': cantidad_ej_ad, 'cant_ej_pr': cantidad_ej_pr, 'titulo': titulo, 'autor': autor}

    return libro_nuevo

def registrar_nuevo_libro():
    nuevo_libro_datos = nuevo_libro() #llamamos a la funcion nuevo_libro() para crear un nuevo libro

    codigo = nuevo_libro_datos['cod']
    encontrado = False

    for libro in libros:
        if libro['cod'] == codigo:
            encontrado = True
    
    if encontrado:
        print("El codigo ya existe")
    else:
        libros.append(nuevo_libro_datos)

        #Mostramos los datos del libro agregado
        print("Se agrego un nuevo libro:")
        print(f"Codigo: {nuevo_libro_datos['cod']}")
        print(f"Ejemplares adquiridos: {nuevo_libro_datos['cant_ej_ad']}")
        print(f"Ejemplares prestados: {nuevo_libro_datos['cant_ej_pr']}")
        print(f"Titulo: {nuevo_libro_datos['titulo']}")
        print(f"Autor: {nuevo_libro_datos['autor']}")