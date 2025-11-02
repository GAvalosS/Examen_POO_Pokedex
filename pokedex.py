class Pokemon:
    nombre = 'Sin Pokémon'
    evos = []
    descripcion = 'No descripción'
    ataque_especial = 'No hay ataque especial'
    ataque = 0
    daño_especial = 0
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
              f'Daño Especial: {self.daño_especial}\n')

    def hablar(self):
        print(f"Pokemon dice: '¡{self.nombre}!'.\n")

    def entrenar(self):
        self.ataque += 10
        self.daño_especial += 11
        self.defensa += 10
        self.vida += 10
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
        
        if self.daño_especial > 1200:
            print(f'\n¡{self.nombre} ha alcanzado el daño especial máximo de 1200!\n')
            self.daño_especial = 1200

    def subirAtaque(self, boostAtaque):
        self.ataque += boostAtaque
        self.daño_especial += boostAtaque + 1
        
        if self.ataque > 1000:
            print(f'\n¡{self.nombre} ha alcanzado el ataque máximo de 1000!\n')
            self.ataque = 1000

        if self.daño_especial > 1200:
            print(f'\n¡{self.nombre} ha alcanzado el daño especial máximo de 1200!\n')
            self.daño_especial = 1200

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

    def __init__(self, nombre, descripcion, ataque, defensa, vida, daño_especial, evolucion=1):
        super().__init__([nombre], descripcion, ataque, defensa, vida, evolucion)
        self.daño_especial = daño_especial

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        super().actualizar(boostAtaque + 5, boostDefensa + 5, boostVida + 5)


class Fuego(Pokemon):
    ataque_especial = 'Lanzallamas'

    def __init__(self, nombre, descripcion, ataque, defensa, vida, daño_especial, evolucion=1):
        super().__init__([nombre], descripcion, ataque, defensa, vida, evolucion)
        self.daño_especial = daño_especial

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        super().actualizar(boostAtaque + 7, boostDefensa + 3, boostVida + 4)


class Electrico(Pokemon):
    ataque_especial = 'Rayo'

    def __init__(self, nombre, descripcion, ataque, defensa, vida, daño_especial, evolucion=1):
        super().__init__([nombre], descripcion, ataque, defensa, vida, evolucion)
        self.daño_especial = daño_especial

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        super().actualizar(boostAtaque + 6, boostDefensa + 4, boostVida + 3)


class Hierba(Pokemon):
    ataque_especial = 'Rayo Solar'

    def __init__(self, nombre, descripcion, ataque, defensa, vida, daño_especial, evolucion=1):
        super().__init__([nombre], descripcion, ataque, defensa, vida, evolucion)
        self.daño_especial = daño_especial

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        super().actualizar(boostAtaque + 4, boostDefensa + 6, boostVida + 5)


PEnemigos = []

PEnemigo = Agua('Squirtle', 'Es una tortuga :D', 240, 325, 220, 260)
evos = ['Squirtle', 'Wartortle', 'Blastoise']
PEnemigo.evos = evos
PEnemigos.append(PEnemigo)

PEnemigo = Fuego('Charmander', 'Es un lagarto :D', 260, 215, 195, 300)
evos = ['Charmander', 'Charmeleon', 'Charizard']
PEnemigo.evos = evos
PEnemigos.append(PEnemigo)

PEnemigo = Electrico('Pikachu', 'Es un ratón :D', 275, 200, 175, 250, evolucion=2)
evos = ['Pichu', 'Pikachu', 'Raichu']
PEnemigo.evos = evos
PEnemigos.append(PEnemigo)

PEnemigo = Hierba('Bulbasaur', 'Es una planta :D', 245, 245, 225, 325)
evos = ['Bulbasaur', 'Ivysaur', 'Venusaur']
PEnemigo.evos = evos
PEnemigos.append(PEnemigo)

misPokemones = []


def verPokemones():
    print('\n--- Tus Pokémons Atrapados ---\n')
    for i in misPokemones:
        i.detallesPokemon()



def mostrarMenu():
    print('\n------ Menú Principal ------\n'
          '1.   Detalles de mi Pokémon\n'
          '2.   Hablar Pokémon.\n'
          '3.   Entrenar Pokémon.\n'
          '4.   Combatir.\n'
          '5.   Ver Pokémon atrapados.\n'
          '6.   Crear Pokémon enemigo.\n'
          '0.   Salir')


def buscarPokemon(pokemon, atrapado):
    i = 1

    if pokemon is None:
        print('Ingresa el nombre de tu Pokémon: ')
        PBuscado = input()
    else:
        PBuscado = pokemon

    if atrapado:
        for p in misPokemones:
            if p.nombre.lower() == PBuscado.lower():
                indice = i - 1
                return indice
            else:
                i += 1

        if i > len(misPokemones):
            print(f'\n¡Oh no, {nombre_usuario}! Parece que aún no tienes ese Pokémon atrapado. UnU\n'
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
            print(f'\n¡Oh no, {nombre_usuario}! Parece que ese Pokémon no existe en la Pokédex. UnU\n'
                  '¿Quieres crear uno nuevo desde el menú principal? :D\n')
            return None

def main():
    print('\n¡Bienvenido al Pokédex!\n')
    global nombre_usuario
    nombre_usuario = input('Por favor, ingresa tu nombre: ')
    print(f'¡Hola, {nombre_usuario}! :)\n\n'
          'De momento, no tienes ningún Pokémon atrapado. :(\n'
          '¡Pero el primero es cortesía de la casa! :D\n\n'
          'Tenemos 4 tipos de Pokémon disponibles:\n'
          '1.     Agua (Squirtle)\n'
          '2.     Fuego (Charmander)\n'
          '3.     Eléctrico (Pikachu)\n'
          '4.     Hierba (Bulbasaur)\n')

    while True:
        eleccion = input('¿Cuál te gustaría atrapar? (Ingresa el número correspondiente): ')
        try:
            eleccion = int(eleccion)
            if eleccion < 1 or eleccion > 4:
                raise ValueError
        except ValueError:
            print('Ups. Parece que ese número no está dentro de las opciones. :(\n'
                  '¿Qué te parece si lo intentas de nuevo? :D\n')
        except TypeError:
            print('Ups. Ese número no lo conozco, mosco. XD \n'
                  '¿Qué te parece si lo intentas de nuevo? :D\n')
        else:
            PDisponibles = PEnemigos
            PElegido = PDisponibles[eleccion - 1]
            PElegido.atrapado = True
            misPokemones.append(PElegido)
            print(f'\n¡Felicidades, {nombre_usuario}! Has atrapado a {PElegido.nombre}.\n'
                  '¡Cuídalo bien y entrenen juntos para convertirse en los mejores!\n')
            break

    print('Aquí están los detalles de tu nuevo Pokémon:\n')
    verPokemones()
    print('Qué gran aventura te espera con tu nuevo amigo. ¡Buena suerte!\n')

    while True:
        mostrarMenu()
        opcion = input(f'¡{nombre_usuario}! Selecciona una opción del menú: ')

        if opcion == '1':
            print('\n¿Qué Pokémon quieres ver?   0.0')
            indice = buscarPokemon(None, True)
            if indice is not None:
                print('\n--- Detalles de tu Pokémon ---\n')
                misPokemones[indice].detallesPokemon()

        elif opcion == '2':
            print('\nHaz que tu Pokémon hable  :D')
            indice = buscarPokemon(None, True)
            if indice is not None:
                misPokemones[indice].hablar()

        elif opcion == '3':
            print('\n--- Entrenamiento de Pokémon ---')
            verPokemones()
            print("Vamos a entrenar a tu Pokémon >:)")
            indice = buscarPokemon(None, True)

            if indice is not None:
                while True:    
                    op = input('\n-----Opciones de entrenamiento:-----\n'
                               '    1-      Entrenamiento normal\n'
                               '    2-      Entrenamiento individual\n'
                               '    3-      Entrenamiento intensivo\n'
                               '    4-      Entrenamiento personalizado\n'
                               '    0-      Salir\n'
                               '-------------------------------------\n'
                               'Seleccione una opción: ')
                
                    if op == '1':
                        misPokemones[indice].entrenar()

                    elif op == '2':
                        estadistica = input('Seleccione la estadística que desea mejorar:\n'
                                            '   -Ataque\n'
                                            '   -Defensa\n'
                                            '   -Vida\n')
                        estadistica.lower()
                        while True:
                            if estadistica == 'ataque':
                                misPokemones[indice].subirAtaque(10)
                                break
                            elif estadistica == 'defensa':
                                misPokemones[indice].subirDefensa(10)
                                break
                            elif estadistica == 'vida':
                                misPokemones[indice].subirVida(10)
                                break
                            else:
                                print('Parece que esa estadística aún no la manejo. :(\n'
                                      '¿Qué te parece si eliges otra? :D\n')
                                estadistica = input('Seleccione la estadística que desea mejorar:\n')

                    elif op == '3':
                        while True:
                            try:
                                boost = int(input('\n¿En cuánto quiere mejorar las estadísticas de su Pokémon?'))
                                break
                            except ValueError:
                                print('Ups. Ese valor no es válido. :p\n')           
                        misPokemones[indice].subirAtaque(boost)
                        misPokemones[indice].subirDefensa(boost)
                        misPokemones[indice].subirVida(boost)

                    elif op == '4':
                        estadistica = input('\nSeleccione la estadística que desea mejorar:\n'
                                            '   -Ataque\n'
                                            '   -Defensa\n'
                                            '   -Vida\n')
                        while True:
                            if estadistica == 'ataque':
                                boost = int(input('¿En cuánto quiere mejorar la estadística de su Pokémon?\n'))
                                misPokemones[indice].subirAtaque(boost)
                                break
                            elif estadistica == 'defensa':
                                boost = int(input('¿En cuánto quiere mejorar la estadística de su Pokémon?\n'))
                                misPokemones[indice].subirDefensa(boost)
                                break
                            elif estadistica == 'vida':
                                boost = int(input('¿En cuánto quiere mejorar la estadística de su Pokémon?\n'))
                                misPokemones[indice].subirVida(boost)
                                break
                            else:
                                print('Estadística inválida')
                                estadistica = input('\nSeleccione la estadística que desea mejorar:\n')
                                break

                    elif op == '0':
                        print('\nSaliendo del entrenamiento de Pokémon.\n')
                        break

                    else:
                        print('\nUps. Parece que aún no existe esa opción. T-T')

                    print('\n¡Muy bien!, las nuevas estadísticas de tu Pokémon son:\n'
                         f'Ataque: {misPokemones[indice].ataque}\n'
                         f'Daño Especial: {misPokemones[indice].daño_especial}\n'
                         f'Defensa: {misPokemones[indice].defensa}\n'
                         f'Vida: {misPokemones[indice].vida}\n'
                         f'Nivel: {misPokemones[indice].nivel}\n')

        elif opcion == '4':
            import random, copy

            plantilla = random.choice(PEnemigos)
            PSalvaje = copy.deepcopy(plantilla)
            copiaMiPokemon = copy.deepcopy(misPokemones[0])

            print('\n--- Combate Pokémon ---\n')
            print(f'¡Un {PSalvaje.nombre} salvaje ha aparecido! :O\n')
            PSalvaje.detallesPokemon()
            print('¿Qué vas a hacer ahora?\n'
                  '     1-  Pasar Turno           2-  Ataque normal\n'
                  '     3-  Ataque especial       0-  Huir')
            
            
            while True:
                accion = input('Selecciona una acción: ')
                if accion == '1':
                    print(f'\n{nombre_usuario} ha decidido pasar el turno.\n')

                elif accion == '2':
                    if PSalvaje.defensa > 0:
                        PSalvaje.defensa -= misPokemones[0].ataque
                        if PSalvaje.defensa < 0:
                            PSalvaje.vida += PSalvaje.defensa
                            PSalvaje.defensa = 0

                    else:
                        PSalvaje.vida -= misPokemones[0].ataque
                        if PSalvaje.vida < 0:
                            PSalvaje.vida = 0
                    
                    print(f'\n¡Tu {misPokemones[0].nombre} ha atacado a {PSalvaje.nombre} salvaje con un ataque normal!\n'
                          f'Defensa de {PSalvaje.nombre}:    {PSalvaje.defensa}.\n'
                          f'Vida de {PSalvaje.nombre}:       {PSalvaje.vida}.\n')

                elif accion == '3':
                    if PSalvaje.defensa > 0:
                        PSalvaje.defensa -= misPokemones[0].daño_especial
                        if PSalvaje.defensa < 0:
                            PSalvaje.vida += PSalvaje.defensa
                            PSalvaje.defensa = 0
                    
                    else:
                        PSalvaje.vida -= misPokemones[0].daño_especial
                    
                    if PSalvaje.vida < 0:
                        PSalvaje.vida = 0
                    
                    print(f'\n¡Tu {misPokemones[0].nombre} ha usado {misPokemones[0].ataque_especial} en {PSalvaje.nombre} salvaje!\n'
                          f'Defensa de {PSalvaje.nombre}:    {PSalvaje.defensa}.\n'
                          f'Vida de {PSalvaje.nombre}:       {PSalvaje.vida}.\n')

                elif accion == '0':
                    print(f'\n{nombre_usuario} ha decidido huir del combate.\n'
                          'Vámonos que aquí espantan.  XD')
                    break

                else:
                    print('Ups. Parece que aún no existe esa opción. T-T\n')

                if PSalvaje.vida <= 0:
                    print(f'\n¡Felicidades, {nombre_usuario}! Has derrotado a {PSalvaje.nombre}.\n')
                    PSalvaje.vida = plantilla.vida
                    PSalvaje.defensa = plantilla.defensa
                    PSalvaje.atrapado = True
                    misPokemones.append(PSalvaje)
                    print(f'¡Has atrapado a {PSalvaje.nombre}!\n')
                    break

                print('~~~~~~~~~~~~~~~~~~~~~~')
                print('¡Es turno del rival!')
                opcionEnemigo = random.randrange(0,9)

                if opcionEnemigo == 1 or opcionEnemigo == 2 or opcionEnemigo == 3 or opcionEnemigo == 4 or opcionEnemigo == 5 or opcionEnemigo == 6 or opcionEnemigo == 7:
                    if misPokemones[0].defensa > 0:
                        misPokemones[0].defensa -= PSalvaje.ataque
                        if misPokemones[0].defensa < 0:
                            misPokemones[0].vida += misPokemones[0].defensa
                            misPokemones[0].defensa = 0

                    else:
                        misPokemones[0].vida -= PSalvaje.ataque
                        if misPokemones[0].vida < 0:
                            misPokemones[0].vida = 0
                    
                    print(f'\n¡{PSalvaje.nombre} salvaje ha atacado a tu {misPokemones[0].nombre} con un ataque normal!\n'
                          f'Defensa de {misPokemones[0].nombre}:    {misPokemones[0].defensa}.\n'
                          f'Vida de {misPokemones[0].nombre}:       {misPokemones[0].vida}.\n')

                elif opcionEnemigo == 8 or opcionEnemigo == 9:
                    if misPokemones[0].defensa > 0:
                        misPokemones[0].defensa -= PSalvaje.daño_especial
                        if misPokemones[0].defensa < 0:
                            misPokemones[0].vida += misPokemones[0].defensa
                            misPokemones[0].defensa = 0

                    else:
                        misPokemones[0].vida -= PSalvaje.daño_especial
                        if misPokemones[0].vida < 0:
                            misPokemones[0].vida = 0
                    
                    print(f'\n¡{PSalvaje.nombre} salvaje ha usado {PSalvaje.ataque_especial} en tu {misPokemones[0].nombre}!\n'
                          f'Defensa de {misPokemones[0].nombre}:    {misPokemones[0].defensa}.\n'
                          f'Vida de {misPokemones[0].nombre}:       {misPokemones[0].vida}.\n')

                elif opcionEnemigo == 0:
                    print(f'\n{PSalvaje.nombre} ha escapado del combate.\n'
                          'Creo que somos demasiado fuertes.  XD')
                    break

                else:
                    pass

                if misPokemones[0].vida <= 0:
                    misPokemones[0].defensa = copiaMiPokemon.defensa
                    misPokemones[0].vida = copiaMiPokemon.vida
                    print(f'{PSalvaje.nombre} nos ha derrotado, tal vez tengamos mas suerte la próxima. TnT')
                    break

                print('~~~~~~~~~~~~~~~~~~~~~~')

        elif opcion == '5':
            verPokemones()
            print('Vas por buen camino, ¡sigue así! :3\n')
            print('------------------------------\n')

        elif opcion == '6':
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
                        raise ValueError
                except ValueError:
                    print('Ups. Ese valor no es válido. :p\n')
                else:
                    break

            evos = [nombre]
            for n in range(i):
                evo_nombre = input(f'Ingresa el nombre de la evolución {n + 1}: ')
                evos.append(evo_nombre)

            descripcion = input('Ingresa una breve descripción del Pokémon: ')

            while True:
                try:
                    ataque = int(input('Ingresa el valor de ataque del Pokémon (1 - 1000): '))
                    if ataque < 1 or ataque > 1000:
                        raise ValueError
                except ValueError:
                    print('Ups. Ese valor no está dentro del rango. :p\n')
                except TypeError:
                    print('Ups. Ese valor no lo conozco, mosco. XD \n')
                else:
                    break

            while True:
                try:
                    defensa = int(input('Ingresa el valor de defensa del Pokémon (1 - 1000): '))
                    if defensa < 1 or defensa > 1000:
                        raise ValueError
                except ValueError:
                    print('Ups. Ese valor no está dentro del rango. :p\n')
                except TypeError:
                    print('Ups. Ese valor no lo conozco, mosco. XD \n')
                else:
                    break

            while True:
                try:
                    vida = int(input('Ingresa el valor de vida del Pokémon (1 - 1000): '))
                    if vida < 1 or vida > 1000:
                        raise ValueError
                except ValueError:
                    print('Ups. Ese valor no está dentro del rango. :p\n')
                except TypeError:
                    print('Ups. Ese valor no lo conozco, mosco. XD \n')
                else:
                    break

            while True:
                try:
                    daño_especial = int(input('Ingresa el valor del daño especial del Pokémon (1 - 1000): '))
                    if daño_especial < 1 or daño_especial > 1000:
                        raise ValueError
                except ValueError:
                    print('Ups. Ese valor no está dentro del rango. :p\n')
                except TypeError:
                    print('Ups. Ese valor no lo conozco, mosco. XD \n')
                else:
                    break

            if tipo == 'agua':
                nuevo_pokemon = Agua(nombre, descripcion, ataque, defensa, vida, daño_especial)
            elif tipo == 'fuego':
                nuevo_pokemon = Fuego(nombre, descripcion, ataque, defensa, vida, daño_especial)
            elif tipo == 'eléctrico':
                nuevo_pokemon = Electrico(nombre, descripcion, ataque, defensa, vida, daño_especial)
            elif tipo == 'hierba':
                nuevo_pokemon = Hierba(nombre, descripcion, ataque, defensa, vida, daño_especial)

            nuevo_pokemon.evos = evos

            PEnemigos.append(nuevo_pokemon)
            print(f"\n¡Nuevo Pokémon enemigo {nuevo_pokemon.nombre} creado exitosamente! :O\n")
            print('Aquí están los detalles de tu nuevo Pokémon enemigo:\n')
            nuevo_pokemon.detallesPokemon()
            print('¡Ahora puedes desafiarlo en combate desde el menú principal! >:)\n')

        elif opcion == '0':
            print(f'\n¡Gracias por usar el Pokédex, {nombre_usuario}! ¡Vuelve pronto! :D\n')
            break

        else:
            print('Ups. Parece que aún no existe esa opción. T-T\n'
                  '¿Qué te parece si intentas una de nuestro menú? :D\n')


main()