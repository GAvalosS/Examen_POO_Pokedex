import os, random, copy, sqlite3, json
from datetime import datetime

# ----------------------
# POKEDEX - VERSIÓN CORREGIDA
# Implementa: carga/guardado con SQLite3, serialización completa
# y restauración de objetos Pokémon. También corrige el flujo de inicio
# para no sobrescribir partidas cargadas.
# ----------------------

class Pokemon:
    nombre = 'Sin Pokémon'
    evos = []
    descripcion = 'No descripción'
    ataque_especial = 'No hay ataque especial'
    ataque = 0
    dano_especial = 0
    defensa = 0
    vida = 0
    nivel = 0
    evolucion = 1
    atrapado = False

    def __init__(self, evos, descripcion, ataque, defensa, vida, evolucion=1):
        self.nombre = evos[0]
        self.evos = evos
        self.descripcion = descripcion
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.evolucion = evolucion

    def detallesPokemon(self):
        print(f'--------- {self.nombre} ---------\n'
              f'Descripción: {self.descripcion}\n'
              f"Atrapado: {'Sí' if self.atrapado else 'No'}\n"
              f'Nivel: {self.nivel}\n'
              f'Evolución: {self.evolucion}\n'
              f'Vida: {self.vida}\n'
              f'Ataque: {self.ataque}\n'
              f'Defensa: {self.defensa}\n'
              f'Ataque Especial: {self.ataque_especial}\n'
              f'Daño Especial: {self.dano_especial}\n')

    def hablar(self):
        print(f"Pokemon dice: '¡{self.nombre}!'.\n")

    def entrenar(self):
        self.ataque += 10
        self.defensa += 10
        self.nivel += 20

        if self.nivel >= 100:
            if self.evolucion < len(self.evos):
                self.evolucion += 1
                print(f'\n¡{self.nombre} ha evolucionado a su fase {self.evolucion}!\n'
                      f'¡Ahora es {self.evos[self.evolucion - 1]}!    :O\n')
                self.nombre = self.evos[self.evolucion - 1]
                self.nivel = 0
            else:
                self.nivel = 100
                print(f'\n¡{self.nombre} ha alcanzado el nivel máximo de evolución!\n')

        if self.ataque > 1000:
            print(f'\n¡{self.nombre} ha alcanzado el ataque máximo de 1000!\n')
            self.ataque = 1000

        if self.defensa > 1000:
            print(f'\n¡{self.nombre} ha alcanzado la defensa máxima de 1000!\n')
            self.defensa = 1000

        if self.vida > 1000:
            print(f'\n¡{self.nombre} ha alcanzado la vida máxima de 1000!\n')
            self.vida = 1000

        if self.dano_especial > 1200:
            print(f'\n¡{self.nombre} ha alcanzado el daño especial máximo de 1200!\n')
            self.dano_especial = 1200

    def subirAtaque(self, boostAtaque):
        self.ataque += boostAtaque
        self.dano_especial += boostAtaque + 1

        if self.ataque > 1000:
            print(f'\n¡{self.nombre} ha alcanzado el ataque máximo de 1000!\n')
            self.ataque = 1000

        if self.dano_especial > 1200:
            print(f'\n¡{self.nombre} ha alcanzado el daño especial máximo de 1200!\n')
            self.dano_especial = 1200

    def subirDefensa(self, boostDefensa):
        self.defensa += boostDefensa
        if self.defensa > 1000:
            print(f'\n¡{self.nombre} ha alcanzado la defensa máxima de 1000!\n')
            self.defensa = 1000

    def subirVida(self, boostVida):
        self.vida += boostVida
        if self.vida > 1000:
            print(f'\n¡{self.nombre} ha alcanzado la vida máxima de 1000!\n')
            self.vida = 1000

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        self.subirAtaque(boostAtaque)
        self.subirDefensa(boostDefensa)
        self.subirVida(boostVida)


class Agua(Pokemon):
    ataque_especial = 'Hidrobomba'

    def __init__(self, nombre, descripcion, ataque, defensa, vida, dano_especial, evolucion=1):
        super().__init__([nombre], descripcion, ataque, defensa, vida, evolucion)
        self.dano_especial = dano_especial

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        super().actualizar(boostAtaque + 5, boostDefensa + 5, boostVida + 5)


class Fuego(Pokemon):
    ataque_especial = 'Lanzallamas'

    def __init__(self, nombre, descripcion, ataque, defensa, vida, dano_especial, evolucion=1):
        super().__init__([nombre], descripcion, ataque, defensa, vida, evolucion)
        self.dano_especial = dano_especial

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        super().actualizar(boostAtaque + 7, boostDefensa + 3, boostVida + 4)


class Electrico(Pokemon):
    ataque_especial = 'Rayo'

    def __init__(self, nombre, descripcion, ataque, defensa, vida, dano_especial, evolucion=1):
        super().__init__([nombre], descripcion, ataque, defensa, vida, evolucion)
        self.dano_especial = dano_especial

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        super().actualizar(boostAtaque + 6, boostDefensa + 4, boostVida + 3)


class Hierba(Pokemon):
    ataque_especial = 'Rayo Solar'

    def __init__(self, nombre, descripcion, ataque, defensa, vida, dano_especial, evolucion=1):
        super().__init__([nombre], descripcion, ataque, defensa, vida, evolucion)
        self.dano_especial = dano_especial

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        super().actualizar(boostAtaque + 4, boostDefensa + 6, boostVida + 5)


PEnemigos = []
misPokemones = []

PEnemigo = Agua('Squirtle', 'Es una tortuga :D', 50, 130, 180, 120)
evos = ['Squirtle', 'Wartortle', 'Blastoise']
PEnemigo.evos = evos
PEnemigos.append(PEnemigo)

PEnemigo = Fuego('Charmander', 'Es un lagarto :D', 55, 95, 160, 125)
evos = ['Charmander', 'Charmeleon', 'Charizard']
PEnemigo.evos = evos
PEnemigos.append(PEnemigo)

PEnemigo = Electrico('Pikachu', 'Es un ratón :D', 80, 110, 190, 110, evolucion=2)
evos = ['Pichu', 'Pikachu', 'Raichu']
PEnemigo.evos = evos
PEnemigos.append(PEnemigo)

PEnemigo = Hierba('Bulbasaur', 'Es una planta :D', 50, 115, 180, 115)
evos = ['Bulbasaur', 'Ivysaur', 'Venusaur']
PEnemigo.evos = evos
PEnemigos.append(PEnemigo)



def pokemon_to_dict(p):
    return {
        'nombre': p.nombre,
        'evos': p.evos,
        'descripcion': p.descripcion,
        'ataque': p.ataque,
        'defensa': p.defensa,
        'vida': p.vida,
        'nivel': p.nivel,
        'evolucion': p.evolucion,
        'atrapado': p.atrapado,
        'dano_especial': p.dano_especial,
        'tipo': p.__class__.__name__
    }


def pokemon_from_dict(d):
    tipo = d.get('tipo', 'Pokemon')
    nombre = d.get('nombre')
    descripcion = d.get('descripcion', 'No descripción')
    ataque = d.get('ataque', 0)
    defensa = d.get('defensa', 0)
    vida = d.get('vida', 0)
    dano_especial = d.get('dano_especial', 0)
    evolucion = d.get('evolucion', 1)
    evos = d.get('evos', [nombre])

    if tipo == 'Agua':
        p = Agua(nombre, descripcion, ataque, defensa, vida, dano_especial, evolucion)
    elif tipo == 'Fuego':
        p = Fuego(nombre, descripcion, ataque, defensa, vida, dano_especial, evolucion)
    elif tipo == 'Electrico':
        p = Electrico(nombre, descripcion, ataque, defensa, vida, dano_especial, evolucion)
    elif tipo == 'Hierba':
        p = Hierba(nombre, descripcion, ataque, defensa, vida, dano_especial, evolucion)
    else:
        # Fallback a Pokemon base
        p = Pokemon(evos, descripcion, ataque, defensa, vida, evolucion)
        p.dano_especial = dano_especial

    p.evos = evos
    p.nivel = d.get('nivel', 0)
    p.atrapado = d.get('atrapado', False)
    return p


# ---------------------------
# Funciones de UI y manejo de archivos de batalla (se mantienen)
# ---------------------------

def verPokemones():
    print('\n--- Tus Pokémons Atrapados ---\n')
    if not misPokemones:
        print('No tienes Pokémons atrapados todavía.\n')
        return
    j = 0
    for i in misPokemones:
        j += 1
        print(f'--------- No. {j} ---------')
        i.detallesPokemon()


def mostrarMenu():
    print('\n========= MENÚ PRINCIPAL =========\n'
          '   (1)     Detalles de mi Pokémon\n'
          '   (2)     Hablar Pokémon.\n'
          '   (3)     Entrenar Pokémon.\n'
          '   (4)     Combatir.\n'
          '   (5)     Ver Pokémon atrapados.\n'
          '   (6)     Crear Pokémon enemigo.\n'
          '   (7)     Prueba de Manejo de Errores.\n'
          '   (8)     Registro de Batallas.\n'
          '   (9)     Guardar Partida.\n'
          '   (0)     Salir.\n'
          '==================================')


def buscarPokemon(pokemon, atrapado):
    i = 1
    j = 0
    repetidos = []
    if pokemon is None:
        PBuscado = input('Ingresa el nombre de tu Pokémon: ')
    else:
        PBuscado = pokemon

    if atrapado:
        for p in misPokemones:
            if p.nombre.lower() == PBuscado.lower():
                indice = i - 1
                repetidos.append(j)
            else:
                i += 1
            j += 1
        i = 0
        if len(repetidos) > 1:
            print('Parece que hay más de un Pokémon con el mismo nombre :O')
            for p in repetidos:
                misPokemones[p].detallesPokemon()
                i += 1
            while True:
                try:
                    op = int(input('Selecciona el que estas buscando\n'))
                    if op > len(repetidos) or op < 1:
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print('Ups, parece que seleccionaste una opción invalida, intente nuevamente con un entero dentro del rango')
            indice = repetidos[op-1]
            return indice
        elif len(repetidos) == 1:
            return indice
        else:
            print(f"\n¡Oh no, {nombre_usuario}! Parece que aún no tienes ese Pokémon atrapado. UnU\n"
                  'Vamos por él. :D\n')
            return None

    else:
        for p in PEnemigos:
            if p.nombre.lower() == PBuscado.lower():
                indice = i - 1
                return indice
            else:
                i += 1

        if i > len(PEnemigos):
            print(f"\n¡Oh no, {nombre_usuario}! Parece que ese Pokémon no existe en la Pokédex. UnU\n"
                  '¿Quieres crear uno nuevo desde el menú principal? :D\n')
            return None


def registro_batallas():
    while True:
        print("\n------- REGISTRO DE BATALLAS -------")
        print("    1.     Ver lista de batallas")
        print("    2.     Leer una batalla")
        print("    3.     Eliminar una batalla")
        print("    0.     Regresar al menú principal")

        opcion = input("Selecciona una opción: ")
        os.system('cls')

        if opcion == "1":
            listar_batallas()

        elif opcion == "2":
            leer_batalla()

        elif opcion == "3":
            eliminar_batalla()

        elif opcion == "0":
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


def listar_batallas():
    print("\n--- Lista de batallas registradas ---")
    archivos = [f for f in os.listdir() if f.startswith("batalla_") and f.endswith(".txt")]

    if not archivos:
        print("No hay registros de batalla.")
        return

    for i, archivo in enumerate(archivos, start=1):
        print(f"{i}. {archivo}")


def leer_batalla():
    listar_batallas()
    archivos = [f for f in os.listdir() if f.startswith("batalla_") and f.endswith(".txt")]

    if not archivos:
        return

    try:
        num = int(input("\nIngresa el número del archivo que deseas leer: ")) - 1

        if num < 0 or num >= len(archivos):
            print("Número inválido.")
            return

        archivo = archivos[num]

        print(f"\n--- {archivo} ---")
        with open(archivo, "r", encoding='utf-8') as f:
            print(f.read())

    except ValueError:
        print("Debes ingresar un número.")


def eliminar_batalla():
    listar_batallas()
    archivos = [f for f in os.listdir() if f.startswith("batalla_") and f.endswith(".txt")]

    if not archivos:
        return

    try:
        num = int(input("\nIngresa el número del archivo que deseas eliminar: ")) - 1

        if num < 0 or num >= len(archivos):
            print("Número inválido.")
            return

        archivo = archivos[num]

        confirm = input(f"¿Seguro que deseas eliminar '{archivo}'? (s/n): ").lower()
        if confirm == "s":
            os.remove(archivo)
            print("Archivo eliminado.")
        else:
            print("Cancelado.")

    except ValueError:
        print("Debes ingresar un número.")


# ---------------------------
# Persistencia SQLite3
# ---------------------------

def crear_tabla(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS partidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_usuario TEXT UNIQUE,
            pokemon_actual TEXT NOT NULL,
            mis_pokemones TEXT NOT NULL,
            fecha TEXT NOT NULL,
            hora TEXT NOT NULL
        )
    """)


def cargar_partida(cursor):
    try:
        cursor.execute("SELECT * FROM partidas")
        partidas = cursor.fetchall()
    except Exception as e:
        print("Error al leer la base de datos:", e)
        return None

    if len(partidas) == 0:
        print("No hay partidas guardadas.")
        return None

    print("\nPARTIDAS GUARDADAS:")
    for i, p in enumerate(partidas, start=1):
        # p: (id, nombre_usuario, pokemon_actual, mis_pokemones, fecha, hora)
        print(f"{i}. [{p[4]} {p[5]}] {p[1]} – {p[2]}")

    while True:
        try:
            eleccion = int(input("Selecciona una partida para continuar: "))
            if eleccion < 1 or eleccion > len(partidas):
                raise ValueError
            break
        except ValueError:
            print("Número inválido.")

    partida = partidas[eleccion - 1]

    nombre = partida[1]
    pokemon_actual = partida[2]
    misPoke_json = partida[3]

    try:
        misPokes_list = json.loads(misPoke_json)
    except Exception:
        misPokes_list = []

    print(f"\n¡Bienvenido de nuevo {nombre}!")
    print(f"Tu Pokémon actual: {pokemon_actual}")

    return nombre, pokemon_actual, misPokes_list


def guardar_partida(cursor, conexion, nombre_usuario, miPokemon, misPokemones):
    fecha = datetime.now().strftime("%d-%m-%Y")
    hora = datetime.now().strftime("%H:%M")

    # Serializar lista completa de pokemons a diccionarios
    lista_serializada = [pokemon_to_dict(p) for p in misPokemones]
    pokemon_actual_nombre = miPokemon.nombre if miPokemon is not None else ''

    try:
        # Usamos INSERT OR REPLACE sobre la columna UNIQUE nombre_usuario
        cursor.execute("""
            INSERT OR REPLACE INTO partidas(nombre_usuario, pokemon_actual, mis_pokemones, fecha, hora)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre_usuario, pokemon_actual_nombre, json.dumps(lista_serializada, ensure_ascii=False), fecha, hora))
        conexion.commit()
        print("\n✔ Partida guardada exitosamente.\n")
    except Exception as e:
        print("Error guardando la partida:", e)


# ---------------------------
# Función para iniciar una partida nueva (elegir Pokémon inicial)
# ---------------------------

def iniciar_partida_nueva():
    print('\n-------------------¡Bienvenido al mundo de:-------------------\n')
    print(r"""                                  ,'\
        _.----.        ____         ,'  _\   ___    ___     ____
    _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
    \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
     \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
       \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
        \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
         \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
          \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
           \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
            \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                    `'                            '-._|
    """)

    nombre_usuario = input('Por favor, ingresa tu nombre: ')
    print(fr'''¡Hola, {nombre_usuario}! :)
    De momento, no tienes ningún Pokémon atrapado. :(
    ¡Pero el primero es cortesía de la casa! :D

    Tenemos 4 tipos de Pokémon disponibles:
    1.     Agua (Squirtle)
    2.     Fuego (Charmander)
    3.     Eléctrico (Pikachu)
    4.     Hierba (Bulbasaur)
    ''')

    # Selección inicial
    while True:
        try:
            eleccion = int(input('¿Cuál te gustaría atrapar? (Ingresa el número correspondiente): '))
        except ValueError:
            print('Ups. Parece que ese número no está dentro de las opciones. :(')
        else:
            if eleccion >= 1 and eleccion <= 4:
                PDisponibles = PEnemigos
                PElegido = PDisponibles[eleccion - 1]
                PElegido = copy.deepcopy(PElegido)
                PElegido.atrapado = True
                misPokemones.append(PElegido)
                os.system('cls')
                print(f'\n¡Felicidades, {nombre_usuario}! Has atrapado a {PElegido.nombre}.\n')
                break
            else:
                print('Ups. Parece que ese número no está dentro de las opciones. :(')

    miPokemon = PElegido
    indice = buscarPokemon(miPokemon.nombre, True)

    print('Aquí están los detalles de tu nuevo Pokémon:\n')
    verPokemones()
    print('Qué gran aventura te espera con tu nuevo amigo. ¡Buena suerte!\n')

    return nombre_usuario, miPokemon


# ---------------------------
# MAIN - flujo principal corregido
# ---------------------------

def main():
    conexion = sqlite3.connect("pokedex.db")
    cursor = conexion.cursor()

    crear_tabla(cursor)

    datos = cargar_partida(cursor)

    partida_cargada = False
    miPokemon = None

    if datos is None:
        op = input("¿Deseas iniciar una nueva partida? (s/n): ").lower()
        if op != "s":
            print("Saliendo del programa...")
            return

        # iniciar nueva partida
        nombre_usuario, miPokemon = iniciar_partida_nueva()

    else:
        nombre_usuario, pokemon_actual_nombre, listaPokes = datos
        partida_cargada = True

        # Reconstruir lista de objetos desde JSON (listaPokes es una lista de diccionarios)
        misPokemones.clear()
        for pd in listaPokes:
            try:
                p = pokemon_from_dict(pd)
                misPokemones.append(p)
            except Exception:
                # si falla la conversión intentamos buscar en plantillas por nombre
                nombre_alt = pd if isinstance(pd, str) else pd.get('nombre', None)
                if nombre_alt:
                    for plantilla in PEnemigos:
                        if plantilla.nombre == nombre_alt:
                            misPokemones.append(copy.deepcopy(plantilla))
                            break

        # Asignar Pokemon actual
        miPokemon = None
        for p in misPokemones:
            if p.nombre == pokemon_actual_nombre:
                miPokemon = p
                break

        # Si no encontramos el pokemon actual, intentar crear a partir de plantillas
        if miPokemon is None and pokemon_actual_nombre:
            for plantilla in PEnemigos:
                if plantilla.nombre == pokemon_actual_nombre:
                    p = copy.deepcopy(plantilla)
                    misPokemones.append(p)
                    miPokemon = p
                    break

        if miPokemon is None:
            # Si aún no hay pokemon actual recogemos uno si hay pokemones disponibles
            if misPokemones:
                miPokemon = misPokemones[0]

        indice = buscarPokemon(miPokemon.nombre, True) if miPokemon else None
        os.system('cls')
        print(f"\n¡Bienvenido de nuevo {nombre_usuario}!")
        if miPokemon:
            print(f"Tu Pokémon actual:")
            miPokemon.detallesPokemon()

    # Si por alguna razón al llegar aquí no tenemos miPokemon (muy improbable), forzamos selección
    if miPokemon is None:
        nombre_usuario, miPokemon = iniciar_partida_nueva()

    indice = buscarPokemon(miPokemon.nombre, True)

    # Bucle principal de menú
    while True:
        mostrarMenu()
        opcion = input(f'¡{nombre_usuario}! Selecciona una opción del menú: ')

        if opcion == '1':
            os.system('cls')
            if indice is not None:
                print('\n--- Detalles de tu Pokémon ---\n')
                misPokemones[indice].detallesPokemon()

        elif opcion == '2':
            os.system('cls')
            print('\nHaz que tu Pokémon hable  :D')
            if indice is not None:
                misPokemones[indice].hablar()

        elif opcion == '3':
            os.system('cls')
            print('\n--- Entrenamiento de Pokémon ---')
            print("Vamos a entrenar a tu Pokémon >:)")

            if indice is not None:
                while True:
                    print('\n-----Opciones de entrenamiento:-----\n'
                          '    1-      Entrenamiento normal\n'
                          '    2-      Entrenamiento individual\n'
                          '    3-      Entrenamiento intensivo\n'
                          '    4-      Entrenamiento personalizado\n'
                          '    0-      Salir\n'
                          '-------------------------------------')
                    op = input('Seleccione una opción: ')
                    os.system('cls')

                    if op == '1':
                        misPokemones[indice].entrenar()

                    elif op == '2':
                        estadistica = input('Seleccione la estadística que desea mejorar:\n'
                                            '   -Ataque     (a)\n'
                                            '   -Defensa    (b)\n'
                                            '   -Vida       (c)\n')
                        estadistica = estadistica.lower()
                        while True:
                            if estadistica == 'a':
                                misPokemones[indice].subirAtaque(10)
                                break
                            elif estadistica == 'b':
                                misPokemones[indice].subirDefensa(10)
                                break
                            elif estadistica == 'c':
                                misPokemones[indice].subirVida(10)
                                break
                            else:
                                print('Parece que esa estadística aún no la manejo. :(')
                                estadistica = input('Seleccione la estadística que desea mejorar:\n')

                    elif op == '3':
                        try:
                            boost = int(input('\n¿En cuánto quiere mejorar las estadísticas de su Pokémon?: '))
                        except ValueError:
                            print('Valor inválido')
                            continue
                        misPokemones[indice].subirAtaque(boost)
                        misPokemones[indice].subirDefensa(boost)
                        misPokemones[indice].subirVida(boost)

                    elif op == '4':
                        estadistica = input('\nSeleccione la estadística que desea mejorar:\n'
                                            '   -Ataque     (a)\n'
                                            '   -Defensa    (b)\n'
                                            '   -Vida       (c)\n')
                        while True:
                            if estadistica == 'a':
                                boost = int(input('¿En cuánto quiere mejorar la estadística de su Pokémon?\n'))
                                misPokemones[indice].subirAtaque(boost)
                                break
                            elif estadistica == 'b':
                                boost = int(input('¿En cuánto quiere mejorar la estadística de su Pokémon?\n'))
                                misPokemones[indice].subirDefensa(boost)
                                break
                            elif estadistica == 'c':
                                boost = int(input('¿En cuánto quiere mejorar la estadística de su Pokémon?\n'))
                                misPokemones[indice].subirVida(boost)
                                break
                            else:
                                print('Estadística inválida')
                                estadistica = input('\nSeleccione la estadística que desea mejorar:\n')

                    elif op == '0':
                        print('\nSaliendo del entrenamiento de Pokémon.\n')
                        break

                    else:
                        print('\nUps. Parece que aún no existe esa opción. T-T')

                    print('\n¡Muy bien!, las nuevas estadísticas de tu Pokémon son:\n'
                          f'Ataque: {misPokemones[indice].ataque}\n'
                          f'Daño Especial: {misPokemones[indice].dano_especial}\n'
                          f'Defensa: {misPokemones[indice].defensa}\n'
                          f'Vida: {misPokemones[indice].vida}\n'
                          f'Nivel: {misPokemones[indice].nivel}\n')

        elif opcion == '4':
            # Combate - se conserva la lógica original (se simplifica levemente manejo de archivos)
            fecha = datetime.now().strftime("%d-%m-%Y")
            hora = datetime.now().strftime("%H-%M-%S")
            nombrearchivo = f"batalla_{fecha}_{hora}.txt"
            try:
                archivo = open(f"{nombrearchivo}", "a", encoding='utf-8')
            except IOError:
                print('No se pudo crear el archivo de batalla. Continuando sin registro de archivo.')
                archivo = None

            os.system('cls')

            plantilla = random.choice(PEnemigos)
            PSalvaje = copy.deepcopy(plantilla)

            print('\n--- Combate Pokémon ---\n')
            print(f'¡Un {PSalvaje.nombre} salvaje ha aparecido! :O\n')
            PSalvaje.detallesPokemon()

            if archivo:
                archivo.write(f"""
                              \n=== COMBATE POKEMON ===\n
Entrenador: {nombre_usuario}
Pokemon: {miPokemon.nombre}
Detalles:
        Vida: {miPokemon.vida}
        Defensa: {miPokemon.defensa}
        Ataque: {miPokemon.ataque}

Enemigo: {PSalvaje.nombre}
Detalles:
        Vida: {PSalvaje.vida}
        Defensa: {PSalvaje.defensa}
        Ataque: {PSalvaje.ataque}

""")

            copiaMiPokemon = copy.deepcopy(misPokemones[indice])

            cargador = 0
            contadorTurno = 1

            while True:
                print('~~~~~~~~~~~~~~~~~~~~~~\n'
                      f'Defensa de {copiaMiPokemon.nombre}:    {copiaMiPokemon.defensa}.\n'
                      f'Vida de {copiaMiPokemon.nombre}:       {copiaMiPokemon.vida} (100%).\n'
                      f'Ataque normal: {copiaMiPokemon.ataque}\n'
                      f'{copiaMiPokemon.ataque_especial}: {copiaMiPokemon.dano_especial}\n')
                print(f'Defensa de {plantilla.nombre}:    {plantilla.defensa}.\n'
                      f'Vida de {plantilla.nombre}:       {plantilla.vida} (100).\n'
                      f'Ataque normal: {plantilla.ataque}\n'
                      f'{plantilla.ataque_especial}: {plantilla.dano_especial}')
                print('~~~~~~~~~~~~~~~~~~~~~~\n')
                print('¿Qué vas a hacer ahora?\n'
                      '     1-  Pasar Turno           2-  Ataque normal\n'
                      '     3-  Ataque especial       0-  Huir')
                accion = input('Selecciona una acción: ')

                if archivo:
                    archivo.write(f"==== TURNO {contadorTurno} ====\n")

                if accion == '1':
                    os.system('cls')
                    print(f'\n{nombre_usuario} ha decidido pasar el turno.\n')
                    if archivo:
                        archivo.write(f'{nombre_usuario} ha decidido pasar el turno.\n\n')

                elif accion == '2':
                    if PSalvaje.defensa > 0:
                        PSalvaje.defensa -= misPokemones[indice].ataque
                        if PSalvaje.defensa < 0:
                            PSalvaje.vida += PSalvaje.defensa
                            PSalvaje.defensa = 0
                        if PSalvaje.vida < 0:
                            PSalvaje.vida = 0

                    else:
                        PSalvaje.vida -= misPokemones[indice].ataque
                        if PSalvaje.vida < 0:
                            PSalvaje.vida = 0

                    os.system('cls')
                    print(
                        f'\n¡Tu {misPokemones[indice].nombre} ha atacado a {PSalvaje.nombre} salvaje con un ataque normal!\n'
                        f'Defensa de {PSalvaje.nombre}:    {PSalvaje.defensa}.\n'
                        f'Vida de {PSalvaje.nombre}:       {PSalvaje.vida} ({(PSalvaje.vida/plantilla.vida*100):.2f}%).\n')
                    cargador += 1

                    if archivo:
                        archivo.write(
                            f'Tu {misPokemones[indice].nombre} ha atacado a {PSalvaje.nombre} salvaje con un ataque normal!\n'
                            f'Defensa de {PSalvaje.nombre}:    {PSalvaje.defensa}.\n'
                            f'Vida de {PSalvaje.nombre}:       {PSalvaje.vida} ({(PSalvaje.vida/plantilla.vida*100):.2f}%).\n\n')

                elif accion == '3':
                    if cargador != 0 and cargador % 3 == 0:
                        if PSalvaje.defensa > 0:
                            PSalvaje.defensa -= misPokemones[indice].dano_especial
                            if PSalvaje.defensa < 0:
                                PSalvaje.vida += PSalvaje.defensa
                                PSalvaje.defensa = 0
                            if PSalvaje.vida < 0:
                                PSalvaje.vida = 0

                        else:
                            PSalvaje.vida -= misPokemones[indice].dano_especial

                        if PSalvaje.vida < 0:
                            PSalvaje.vida = 0

                        os.system('cls')
                        print(
                            f"\n¡Tu {misPokemones[indice].nombre} ha usado {misPokemones[indice].ataque_especial} en {PSalvaje.nombre} salvaje!\n"
                            f"Defensa de {PSalvaje.nombre}:    {PSalvaje.defensa}.\n"
                            f"Vida de {PSalvaje.nombre}:       {PSalvaje.vida} ({(PSalvaje.vida/plantilla.vida*100):.2f}%).\n")

                        if archivo:
                            archivo.write(
                                f'Tu {misPokemones[indice].nombre} ha usado {misPokemones[indice].ataque_especial} en {PSalvaje.nombre} salvaje!\n'
                                f'Defensa de {PSalvaje.nombre}:    {PSalvaje.defensa}.\n'
                                f'Vida de {PSalvaje.nombre}:       {PSalvaje.vida} ({(PSalvaje.vida/plantilla.vida*100):.2f}%).\n\n')

                    else:
                        os.system('cls')
                        print("No abuses de tus ataques especiales >:T")
                        if archivo:
                            archivo.write(f"{nombre_usuario} quiso abusar de sus ataques especiales.\n\n")

                elif accion == '0':
                    print(f"\n{nombre_usuario} ha decidido huir del combate.\nVámonos que aquí espantan.  XD")
                    if archivo:
                        archivo.write(f"{nombre_usuario} ha decidido huir del combate.\n\n")
                    break

                else:
                    print('Ups. Parece que aún no existe esa opción. T-T\n')

                if PSalvaje.vida <= 0:
                    print(f"\n¡Felicidades, {nombre_usuario}! Has derrotado a {PSalvaje.nombre}.\n")
                    PSalvaje.vida = plantilla.vida
                    PSalvaje.defensa = plantilla.defensa
                    PSalvaje.atrapado = True
                    misPokemones.append(PSalvaje)
                    print(f'¡Has atrapado a {PSalvaje.nombre}!\n')
                    if archivo:
                        archivo.write(f"\nResultado: Victoria! Has derrotado al Pokemon enemigo y lo has atrapado!\n")
                    break

                print()
                print('¡Es turno del rival!')
                opcionEnemigo = random.randrange(0, 9)

                if opcionEnemigo in range(1, 8):
                    if misPokemones[indice].defensa > 0:
                        misPokemones[indice].defensa -= PSalvaje.ataque
                        if misPokemones[indice].defensa < 0:
                            misPokemones[indice].vida += misPokemones[indice].defensa
                            misPokemones[indice].defensa = 0

                    else:
                        misPokemones[indice].vida -= PSalvaje.ataque
                        if misPokemones[indice].vida < 0:
                            misPokemones[indice].vida = 0

                    print(
                        f"\n¡{PSalvaje.nombre} salvaje ha atacado a tu {misPokemones[indice].nombre} con un ataque normal!\n"
                        f"Defensa de {misPokemones[indice].nombre}:    {misPokemones[indice].defensa}.\n"
                        f"Vida de {misPokemones[indice].nombre}:       {misPokemones[indice].vida} ({(misPokemones[indice].vida/copiaMiPokemon.vida*100):.2f}%).\n")

                    if archivo:
                        archivo.write(
                            f'{PSalvaje.nombre} salvaje ha atacado a tu {misPokemones[indice].nombre} con un ataque normal!\n'
                            f'Defensa de {misPokemones[indice].nombre}:    {misPokemones[indice].defensa}.\n'
                            f'Vida de {misPokemones[indice].nombre}:       {misPokemones[indice].vida} ({(misPokemones[indice].vida/copiaMiPokemon.vida*100):.2f}%).\n\n')

                elif opcionEnemigo in (8, 9):
                    if misPokemones[indice].defensa > 0:
                        misPokemones[indice].defensa -= PSalvaje.dano_especial
                        if misPokemones[indice].defensa < 0:
                            misPokemones[indice].vida += misPokemones[indice].defensa
                            misPokemones[indice].defensa = 0

                    else:
                        misPokemones[indice].vida -= PSalvaje.dano_especial
                        if misPokemones[indice].vida < 0:
                            misPokemones[indice].vida = 0

                    print(
                        f"\n¡{PSalvaje.nombre} salvaje ha usado {PSalvaje.ataque_especial} en tu {misPokemones[indice].nombre}!\n"
                        f"Defensa de {misPokemones[indice].nombre}:    {misPokemones[indice].defensa}.\n"
                        f"Vida de {misPokemones[indice].nombre}:       {misPokemones[indice].vida} ({(misPokemones[indice].vida/copiaMiPokemon.vida*100):.2f}%).\n")

                    if archivo:
                        archivo.write(
                            f'{PSalvaje.nombre} salvaje ha usado {PSalvaje.ataque_especial} en tu {misPokemones[indice].nombre}!\n'
                            f'Defensa de {misPokemones[indice].nombre}:    {misPokemones[indice].defensa}.\n'
                            f'Vida de {misPokemones[indice].nombre}:       {misPokemones[indice].vida} ({(misPokemones[indice].vida/copiaMiPokemon.vida*100):.2f}%).\n\n')

                elif opcionEnemigo == 0:
                    print(f"\n{PSalvaje.nombre} ha escapado del combate.\nCreo que somos demasiado fuertes.  XD")
                    if archivo:
                        archivo.write(f"{PSalvaje.nombre} escapó del combate.\n")
                    break

                if misPokemones[indice].vida <= 0:
                    misPokemones[indice].defensa = copiaMiPokemon.defensa
                    misPokemones[indice].vida = copiaMiPokemon.vida
                    print(f'{PSalvaje.nombre} nos ha derrotado, tal vez tengamos mas suerte la próxima. TnT')
                    if archivo:
                        archivo.write(f"\nResultado: Derrota! {PSalvaje.nombre} nos ha vencido.")
                    break

                contadorTurno += 1

            # restaurar stats y cerrar archivo
            misPokemones[indice].vida = copiaMiPokemon.vida
            misPokemones[indice].defensa = copiaMiPokemon.defensa
            if archivo:
                archivo.write(f"\n\nFecha y hora de la batalla: {fecha} {hora}")
                archivo.close()

        elif opcion == '5':
            os.system('cls')
            verPokemones()
            print('Vas por buen camino, ¡sigue así! :3\n')
            print('------------------------------\n')

            while True:
                cambiar = input('¿Deseas cambiar de pokemon? (s/n): ')
                if cambiar.lower() == 's':
                    try:
                        noPokemon = int(input('Ingrese el número de pokemon: '))
                        if noPokemon < 1 or noPokemon > len(misPokemones):
                            raise ValueError
                    except ValueError:
                        print('Ups. Ese número no está en la lista.')
                    else:
                        miPokemon = misPokemones[noPokemon - 1]
                        indice = buscarPokemon(miPokemon.nombre, True)
                        os.system('cls')
                        print(f'\n¡Haz elegido a {miPokemon.nombre}!')
                        miPokemon.detallesPokemon()
                        print('¡Que continúe la aventura! >:D\n')
                        break
                elif cambiar.lower() == 'n':
                    print('De acuerdo. :D\n')
                    break
                else:
                    print('Ups, no sé interpretar eso Unu.\n')

        elif opcion == '6':
            os.system('cls')
            print('Excelente, vamos a crear un nuevo Pokémon enemigo para que puedas combatir.\n')

            while True:
                tipo = input('Ingresa el tipo de Pokémon (Agua, Fuego, Eléctrico, Hierba): ').strip().lower()
                if tipo in ['agua', 'fuego', 'eléctrico', 'hierba']:
                    break
                else:
                    print('Ups. Ese tipo de Pokémon no existe. U.U\n')

            nombre = input('Ingresa el nombre del Pokémon: ').strip()

            while True:
                try:
                    i = int(input('¿Cuántas evoluciones adicionales tendrá el Pokémon? (0 si no tiene): '))
                    if i < 0 or i > 2:
                        print('Ups. Ese valor no es válido. :p\n')
                    else:
                        break
                except ValueError:
                    print('Introduzca la cantidad como un número entero')

            evos = [nombre]
            for n in range(i):
                evo_nombre = input(f'Ingresa el nombre de la evolución {n + 1}: ')
                evos.append(evo_nombre)

            descripcion = input('Ingresa una breve descripción del Pokémon: ')

            while True:
                try:
                    ataque = int(input('Ingresa el valor de ataque del Pokémon (1 - 1000): '))
                    if ataque < 1 or ataque > 1000:
                        print('Ups. Ese valor no está dentro del rango. :p\n')
                    else:
                        break
                except ValueError:
                    print('Introduzca la cantidad como un número entero')

            while True:
                try:
                    defensa = int(input('Ingresa el valor de defensa del Pokémon (1 - 1000): '))
                    if defensa < 1 or defensa > 1000:
                        print('Ups. Ese valor no está dentro del rango. :p\n')
                    else:
                        break
                except ValueError:
                    print('Introduzca la cantidad como un número entero')

            while True:
                try:
                    vida = int(input('Ingresa el valor de vida del Pokémon (1 - 1000): '))
                    if vida < 1 or vida > 1000:
                        print('Ups. Ese valor no está dentro del rango. :p\n')
                    else:
                        break
                except ValueError:
                    print('Introduzca la cantidad como un número entero')

            while True:
                try:
                    dano_especial = int(input('Ingresa el valor del daño especial del Pokémon (1 - 1000): '))
                    if dano_especial < 1 or dano_especial > 1000:
                        print('Ups. Ese valor no está dentro del rango. :p\n')
                    else:
                        break
                except ValueError:
                    print('Introduzca la cantidad como un número entero')

            if tipo == 'agua':
                nuevo_pokemon = Agua(nombre, descripcion, ataque, defensa, vida, dano_especial)
            elif tipo == 'fuego':
                nuevo_pokemon = Fuego(nombre, descripcion, ataque, defensa, vida, dano_especial)
            elif tipo == 'eléctrico':
                nuevo_pokemon = Electrico(nombre, descripcion, ataque, defensa, vida, dano_especial)
            elif tipo == 'hierba':
                nuevo_pokemon = Hierba(nombre, descripcion, ataque, defensa, vida, dano_especial)

            nuevo_pokemon.evos = evos

            PEnemigos.append(nuevo_pokemon)
            print(f"\n¡Nuevo Pokémon enemigo {nuevo_pokemon.nombre} creado exitosamente! :O\n")
            print('Aquí están los detalles de tu nuevo Pokémon enemigo:\n')
            nuevo_pokemon.detallesPokemon()
            print('¡Ahora puedes desafiarlo en combate desde el menú principal! >:)\n')

        elif opcion == '7':
            # Pruebas de Manejo de Errores (ejemplos)
            os.system('cls')
            print('\n--- Pruebas de Manejo de Errores ---')
            print('1) Intentar dividir entre cero (ZeroDivisionError)')
            print('2) Intentar acceso fuera de rango (IndexError)')
            print('3) Intentar convertir texto a entero (ValueError)')
            print('0) Volver')
            op = input('Selecciona una prueba: ')

            if op == '1':
                try:
                    _ = 1 / 0
                except ZeroDivisionError:
                    print('Se capturó ZeroDivisionError: no es posible dividir entre cero.')
            elif op == '2':
                try:
                    a = [1, 2]
                    _ = a[5]
                except IndexError:
                    print('Se capturó IndexError: índice fuera de rango.')
            elif op == '3':
                try:
                    int('hola')
                except ValueError:
                    print('Se capturó ValueError: conversión inválida.')
            else:
                pass

        elif opcion == '8':
            os.system('cls')
            registro_batallas()

        elif opcion == '9':
            confirmar = input("¿Deseas guardar el progreso actual? (s/n): ").lower()
            if confirmar == "s":
                guardar_partida(cursor, conexion, nombre_usuario, miPokemon, misPokemones)
            else:
                print("No se guardó la partida.\n")

        elif opcion == '0':
            print(f'\n¡Gracias por usar el Pokédex, {nombre_usuario}! ¡Vuelve pronto! :D\nMe piro vampiro\n')
            try:
                conexion.close()
            except Exception:
                pass
            break

        else:
            os.system('cls')
            print('Ups. Parece que aún no existe esa opción. T-T\n'
                  '¿Qué te parece si intentas una de nuestro menú? :D\n')


if __name__ == '__main__':
    main()
