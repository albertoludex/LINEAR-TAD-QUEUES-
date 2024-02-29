# Autor: Alberto Ludeña Peirado
from queue import Queue
import queue
import random
import time

# Definimos las constantes que usaremos en la simulación
NUMERO_DE_SALAS = 3
SALA_TAMANO = 10


"""TENEMOS QUE HACER EL APARTADO 1 DEL MENU--------------HECHO"""
"""TENEMOS QUE HACER EL APARTADO 2 DEL MENU--------------HECHO"""
"""TENEMOS QUE HACER EL APARTADO 3 DEL MENU--------------HECHO"""
"""TENEMOS QUE HACER EL APARTADO 4 DEL MENU--------------HECHO"""
"""TENEMOS QUE HACER EL APARTADO 5 DEL MENU--------------HECHO"""
"""TENEMOS QUE HACER EL APARTADO 6 DEL MENU--------------HECHO"""
"""TENEMOS QUE HACER EL APARTADO 7 DEL MENU--------------HECHO"""
sala_a = []
sala_b = []
sala_c = []

# Creamos las tres colas que seran globales
cola_1 = queue.Queue()
cola_2 = queue.Queue()
cola_3 = queue.Queue()
colas = [cola_1, cola_2, cola_3]
lista_usuarios = []
usuarios = []


# Función para crear un diccionario de usuario
def sacar_user():
    print("Ha elegido la opción 1")
    # Pedimos el ID del usuario
    while True:
        try:
            id_usuario = int(
                input(
                    "Introduce el ID del usuario (debe ser un número entre 0 y 999999): "
                )
            )
            if id_usuario < 0 or id_usuario > 999999:
                print("El ID del usuario no es válido. Por favor, inténtelo de nuevo.")
            else:
                break
        except ValueError:
            print(
                "El ID del usuario debe ser un número entero. Por favor, inténtelo de nuevo."
            )

    # Pedimos el nombre del usuario
    while True:
        nombre = input("Introduce el nombre del usuario (máximo 10 caracteres): ")
        if not nombre.isalpha() or len(nombre) > 10:
            print("El nombre del usuario no es válido. Por favor, inténtelo de nuevo.")
        else:
            break

    # Pedimos la edad del usuario
    while True:
        try:
            edad = int(input("Introduce la edad del usuario (debe ser un número entre 0 y 99): ")
            )
            if edad < 0 or edad > 99:print("La edad del usuario no es válida. Por favor, inténtelo de nuevo.")
            else:
                break
        except ValueError:
            print("La edad del usuario debe ser un número entero. Por favor, inténtelo de nuevo.")

    # Pedimos el género del usuario
    while True:
        genero = input("Introduce el género del usuario (masculino, femenino u otro): ")
        if genero not in ["masculino", "femenino", "otro"]:
            print("El género del usuario no es válido. Por favor, inténtelo de nuevo.")
        else:
            break

    # Pedimos el tipo de cine que quiere ver el usuario
    while True:
        tipo_cine = input(
            "Introduce el tipo de cine que desea ver (comedia, terror o fantasia): "
        )
        if tipo_cine not in ["comedia", "terror", "fantasia"]:
            print("El tipo de cine no es válido. Por favor, inténtelo de nuevo.")
        else:
            break

    # Preguntamos si el usuario quiere entrada o no
    while True:
        entrada = input("¿El usuario quiere entrada? (si o no): ")
        if entrada not in ["si", "no"]:
            print("La respuesta no es válida. Por favor, inténtelo de nuevo.")
        else:
            break

    # Creamos el diccionario con los datos del usuario y lo devolvemos
    usuario_generador = {
        "id": id_usuario,
        "nombre": nombre,
        "edad": edad,
        "género": genero,
        "tipo_cine": tipo_cine,
        "entrada": entrada,
    }
    return usuario_generador


# Opcion uno sirve para poder meter un usuario en la cola pidiendo cada uno de los campos que tiene que tener el usuario
def opcion1():
    # Pedimos al usuario que ingrese los datos del usuario
    usuario_generador = sacar_user()

    while True:
        # Pedimos al usuario que indique a qué cola desea agregar el usuario
        cola_num = int(
            input("Ingrese el número de cola donde desea agregar el usuario (1, 2 o 3): "))

        # Agregamos el usuario a la cola especificada
        if cola_num == 1:
            cola_1.put(usuario_generador)
            # Imprimir cada usuario en una nueva línea
        elif cola_num == 2:
            cola_2.put(usuario_generador)
        elif cola_num == 3:
            cola_3.put(usuario_generador)
        else:
            print("El número de cola especificado no es válido")

        # Mostramos el contenido de las tres colas después de agregar el usuario
        print("Contenido de la cola 1:")
        for nombre in cola_1.queue:
            print(nombre)
        print("Contenido de la cola 2:")
        for nombre in cola_2.queue:
            print(nombre)
        print("Contenido de la cola 3:")
        for nombre in cola_3.queue:
            print(nombre)

        break

    # Opcion dos que la usaremos parar poder sacar el usuario de la cola que nosotros elijamos


def opcion2():
    # Checking if any of the queues are empty before displaying their contents
    if cola_1.empty():
        print("La cola 1 está vacía")
    else:
        print("Contenido de la cola 1:")
        for nombre in cola_1.queue:
            print(nombre)

    if cola_2.empty():
        print("La cola 2 está vacía")
    else:
        print("Contenido de la cola 2:")
        for nombre in cola_2.queue:
            print(nombre)

    if cola_3.empty():
        print("La cola 3 está vacía")
    else:
        print("Contenido de la cola 3:")
        for nombre in cola_3.queue:
            print(nombre)

    # Pedimos al usuario que indique de qué cola desea sacar el usuario

    cola_num = int(input("Ingrese el número de cola de donde desea sacar el usuario (1, 2 o 3): "))

    # Check if the selected queue is empty before dequeuing the element
    if cola_num == 1:
        if cola_1.empty():
            print("La cola 1 está vacía, no se puede sacar un usuario.")
        else:
            print("El usuario ha sido sacado de la cola 1")
            print(cola_1.get())
    elif cola_num == 2:
        if cola_2.empty():
            print("La cola 2 está vacía, no se puede sacar un usuario.")
        else:
            print("El usuario ha sido sacado de la cola 2")
            print(cola_2.get())
    elif cola_num == 3:
        if cola_3.empty():
            print("La cola 3 está vacía, no se puede sacar un usuario.")
        else:
            print("El usuario ha sido sacado de la cola 3")
            print(cola_3.get())
    else:
        print("El número de cola especificado no es válido")


def opcion3():
    print("Ha seleccionado la opción 3")

    cola_seleccionada = random.choice(colas)
    elementos = list(cola_seleccionada.queue)
    random.shuffle(elementos)

    print(f"Elementos de la cola {colas.index(cola_seleccionada)+1}:\n {elementos}")

def opcion4():
    while True:
        print("Ha seleccionado la opción 4")
        # Mostramos el contenido actual de las tres colas
        if cola_1.empty() and cola_2.empty() and cola_3.empty():
            print("No hay clientes esperando en ninguna cola.")
        else:
            print("Clientes esperando en la cola 1:")
            for usuario_generador in cola_1.queue:
                print(usuario_generador)
            print("Clientes esperando en la cola 2:")
            for usuario_generador in cola_2.queue:
                print(usuario_generador)
            print("Clientes esperando en la cola 3:")
            for usuario_generador in cola_3.queue:
                print(usuario_generador)
        break


def opcion5():
    print("ha seleccionado la opción 5")
    # Se pide al usuario que indique que id quiere buscar
    id_buscado = int(input("Ingrese el ID del usuario que desea buscar: "))

    # Se define variable flag para indicar si se encontró al usuario o no
    usuario_encontrado = False

    # Recorremos la cola 1
    for usuario in cola_1.queue:
        if usuario["id"] == id_buscado:
            print("El usuario se encuentra en la Cola 1:")
            print(usuario)

            # Cambiamos el valor de la variable para reflejar que lo encontramos
            usuario_encontrado = True
            break

    # Recorremos la cola 2
    if not usuario_encontrado:
        for usuario in cola_2.queue:
            if usuario["id"] == id_buscado:
                print("El usuario se encuentra en la Cola 2:")
                print(usuario)

                # Cambiamos el valor de la variable para reflejar que lo encontramos
                usuario_encontrado = True
                break

    # Recorremos la cola 3
    if not usuario_encontrado:
        for usuario in cola_3.queue:
            if usuario["id"] == id_buscado:
                print("El usuario se encuentra en la Cola 3:")
                print(usuario)

                # Cambiamos el valor de la variable para reflejar que lo encontramos
                usuario_encontrado = True
                break

    # Verificamos si conseguimos el usuario o no
    if not usuario_encontrado:
        print("El usuario no se encuentra en ninguna cola")


def generar_usuario():
    id_tarjeta = random.randrange(100000, 999999)
    nombres = [
        "Alberto","Juan","Pedro","Maria","Luis","Jose", "Antonio", "Manuel", "Francisco","Miguel","Luis","Jesus","David","Jose","Rafael","Carlos","Javier","Daniel","Jose","Pablo","Marcelino","Alejandro","Jose","Angel", "Jose","Miguel","Jose","Sergio","Jose","Ivan","Jose","Juan","Jose",]
    nombre = random.choice(nombres)
    edad = random.randrange(1, 99)
    generos = ["masculino", "femenino", "otro"]
    genero = random.choice(generos)
    tipo_cine = ["comedia", "terror", "fantasia"]
    tipo_cine = random.choice(tipo_cine)
    entrada = ["si", "no"]
    entrada = random.choice(entrada)

    usuario = {
        "id": id_tarjeta,
        "nombre": nombre,
        "edad": edad,
        "genero": genero,
        "tipo_cine": tipo_cine,
        "entrada": entrada,
    }

    return usuario


def opcion6():
    print("Ha seleccionado la opción 6")
    print("Inicializando simulación...")

    colas = [queue.Queue(), queue.Queue(), queue.Queue()]
    sala_a, sala_b, sala_c = [], [], []
    start_time = time.time()


    while True:
        try:
            usuario = generar_usuario()
            print(f"--> Se ha creado el usuario: {usuario}")

            cola_seleccionada = random.choice(colas)
            cola_seleccionada.put(usuario)
            print(
                f"--> Usuario agregado a la cola {colas.index(cola_seleccionada) + 1}.\n"
            )

            if usuario["tipo_cine"] == "comedia":
                if len(sala_a) < 10:
                    sala_a.append(usuario)
                    print( f"EVENTO: Entrada al cliente {usuario['id']} para la sala A (Satisfecho).")
                else:
                    print(f"EVENTO: Entrada al cliente {usuario['id']} para la sala A (Insatisfecho, B).")
            elif usuario["tipo_cine"] == "terror":
                if len(sala_b) < 10:
                    sala_b.append(usuario)
                    print(f"EVENTO: Entrada al cliente {usuario['id']} para la sala B (Satisfecho).")
                else:
                    print(f"EVENTO: Entrada al cliente {usuario['id']} para la sala B (Insatisfecho, A o C).")
            elif usuario["tipo_cine"] == "fantasia":
                if len(sala_c) < 10:
                    sala_c.append(usuario)
                    print(f"EVENTO: Entrada al cliente {usuario['id']} para la sala C (Satisfecho).")
                else:
                    print(f"EVENTO: Entrada al cliente {usuario['id']} para la sala C (Insatisfecho, B).\n")

            if len(sala_a) == 10 and len(sala_b) == 10 and len(sala_c) == 10:
                print("Las salas están llenas. La simulación finaliza.")
                break

            if (time.time() - start_time) >= 30:
                print("El tiempo de ejecución ha terminado. La simulación finaliza")
                break
            if random.random() <= 0.05:
                numero_random = random.randint(1, 3)
                # Agregar al usuario a la cola correspondiente
                print(f"\n--> Usuario {usuario['id']} tuvo un problema con la tarjeta y fue devuelto a la cola {numero_random}.\n")

                colas[numero_random - 1].put(usuario)

            time.sleep(5)

        except KeyboardInterrupt:
            print("\nInterrupción detectada. La simulación finaliza.\n")
            break

        except Exception as e:
            print(f"Error: {e}. La simulación finaliza.")
            break

    for i, cola in enumerate(colas):
        print(f"- Estado de la cola {i+1}:")
        elementos = list(cola.queue)[:10]
        for elemento in elementos:
            print(elemento)

    print(f"SALA A: {len(sala_a)} personas | SALA B: {len(sala_b)} personas | SALA C: {len(sala_c)} personas")
    if len(sala_a) == 10 and len(sala_b) == 10 and len(sala_c) == 10:
        print(f"---> Todas las salas están llenas.")
    else:
        print(f"---> Salas disponibles: {'A' if len(sala_a) < 10 else ''}{'B' if len(sala_b) < 10 else ''}{'C' if len(sala_c) < 10 else ''}")

    print("La simulación ha concluido")


def opcion7():
    print("Gracias por usar nuestro programa, hasta pronto")
    exit()


# Aqui vamos a por todo el tema relacionado con el menu
while True:
    print("Bienvenido al menu:")
    print("1. Insertar un miembro de la cola")
    print("2. Sacar un miembro de la cola")
    print("3. Imprimir cualquier cola")
    print("4. Consultar que clientes estan esperando en cualquier cola")
    print("5. Ver informacion de un cliente a traves de un id")
    print("6. Iniciar la simulacion, datos generados aleatoriamente o de fichero")
    print("7. Salir de la aplicacion ")
    opcion = input("Ingresa el número de opción: ")

    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        opcion3()
    elif opcion == "4":
        opcion4()
    elif opcion == "5":
        opcion5()
    elif opcion == "6":
        opcion6()
    elif opcion == "7":
        opcion7()
    else:
        print("Opción no válida")