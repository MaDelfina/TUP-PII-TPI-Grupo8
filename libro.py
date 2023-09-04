import cod_generator
import bibloteca

# Crear un diccionario para cada libro
libro1 = {'cod': 'cod1', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'cod2', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'cod3', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    bibloteca.registrar_nuevo_libro()
    return None

def generar_codigo():
    cod_generator.generar()
    return None