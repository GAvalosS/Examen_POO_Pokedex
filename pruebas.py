class Pokemon:
    nombre = 'Sin Pokémon'
    descripcion = 'No descripción'
    ataque_especial = 'No hay ataque especial'
    ataque = 0
    daño_especial = 0
    defensa = 0
    vida = 0
    nivel = 0
    evolucion = 1
    atrapado = False

    def __init__(self, nombre, descripcion, ataque, defensa, vida, evolucion=1):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.evolucion = evolucion

    def detallesPokemon(self):
        print(f'--------- {self.nombre} ---------\n'
              f'Descripción: {self.descripcion}\n'
              f'Atrapado: {'Sí' if self.atrapado else 'No'}\n'
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
            self.evolucion += 1
            print(f'¡{self.nombre} ha evolucionado a su fase {self.evolucion}!\n')
            self.nivel = 0


        

    def subirAtaque(self, boostAtaque):
        self.ataque += boostAtaque
        self.daño_especial += boostAtaque + 1

    def subirDefensa(self, boostDefensa):
        self.defensa += boostDefensa

    def subirVida(self, boostVida):
        self.vida += boostVida

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        self.subirAtaque(boostAtaque)
        self.subirDefensa(boostDefensa)
        self.subirVida(boostVida)


class Agua(Pokemon):
    ataque_especial = 'Hidrobomba'

    def __init__(self, nombre, descripcion, ataque, defensa, vida, daño_especial, evolucion=1):
        super().__init__(nombre, descripcion, ataque, defensa, vida, evolucion)
        self.daño_especial = daño_especial

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        super().actualizar(boostAtaque + 5, boostDefensa + 5, boostVida + 5)


class Fuego(Pokemon):
    ataque_especial = 'Lanzallamas'

    def __init__(self, nombre, descripcion, ataque, defensa, vida, daño_especial, evolucion=1):
        super().__init__(nombre, descripcion, ataque, defensa, vida, evolucion)
        self.daño_especial = daño_especial

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        super().actualizar(boostAtaque + 7, boostDefensa + 3, boostVida + 4)


class Electrico(Pokemon):
    ataque_especial = 'Rayo'

    def __init__(self, nombre, descripcion, ataque, defensa, vida, daño_especial, evolucion=1):
        super().__init__(nombre, descripcion, ataque, defensa, vida, evolucion)
        self.daño_especial = daño_especial

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        super().actualizar(boostAtaque + 6, boostDefensa + 4, boostVida + 3)


class Hierba(Pokemon):
    ataque_especial = 'Rayo Solar'

    def __init__(self, nombre, descripcion, ataque, defensa, vida, daño_especial, evolucion=1):
        super().__init__(nombre, descripcion, ataque, defensa, vida, evolucion)
        self.daño_especial = daño_especial

    def actualizar(self, boostAtaque, boostDefensa, boostVida):
        super().actualizar(boostAtaque + 4, boostDefensa + 6, boostVida + 5)


PEnemigos = []

PEnemigo = Agua('Squirtle', 'Es una tortuga :D', 240, 325, 220, 260)
PEnemigos.append(PEnemigo)
PEnemigo = Fuego('Charmander', 'Es un lagarto :D', 260, 215, 195, 300)
PEnemigos.append(PEnemigo)
PEnemigo = Electrico('Pikachu', 'Es un ratón :D', 275, 200, 175, 250)
PEnemigos.append(PEnemigo)
PEnemigo = Hierba('Bulbasaur', 'Es una planta :D', 245, 245, 225, 325)
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


def buscarPokemon():
    i = 1
    PBuscado = input()
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
            print('\nIngresa el nombre de tu Pokémon para ver sus detalles: ')
            indice = buscarPokemon()
            if indice is not None:
                print('\n--- Detalles de tu Pokémon ---\n')
                misPokemones[indice].detallesPokemon()

        elif opcion == '2':
            print('\nIngresa el nombre de tu Pokémon para que hable: ')
            indice = buscarPokemon()
            if indice is not None:
                misPokemones[indice].hablar()

        elif opcion == '3':
            print('\n--- Entrenamiento de Pokémon ---')
            print("\nSeleccione al Pokémon que desea entrenar")
            verPokemones()
            indice = buscarPokemon()

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

                elif op == '3':
                    boost = int(input('\n¿En cuánto quiere mejorar las estadísticas de su Pokémon?'))
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
                            boost = int(input('¿En cuánto quiere mejorar la estadística de su Pokémon?'))
                            misPokemones[indice].subirAtaque(boost)
                            break
                        elif estadistica == 'defensa':
                            boost = int(input('¿En cuánto quiere mejorar la estadística de su Pokémon?'))
                            misPokemones[indice].subirDefensa(boost)
                            break
                        elif estadistica == 'vida':
                            boost = int(input('¿En cuánto quiere mejorar la estadística de su Pokémon?'))
                            misPokemones[indice].subirVida(boost)
                            break
                        else:
                            print('Elija una estadística válida')

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
            import random
            PSalvaje = random.choice(PEnemigos)
            print(f'¡Un {PSalvaje} ha aparecido!\n'
                  f'{PSalvaje.detallesPokemon()}'
                  '¿Qué vas a hacer ahora?\n'
                  '1-Pasar Turno      2-Ataque normal\n'
                  '3-Ataque especial  3-Huir')

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

            nombre = input('Ingresa el nombre del Pokémon: ')
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

            PEnemigos.append(nuevo_pokemon)
            print(f'\n¡Nuevo Pokémon enemigo {nombre} creado exitosamente! :O\n')
            print('Aquí están los detalles de tu nuevo Pokémon enemigo:\n')
            nuevo_pokemon.detallesPokemon()
            print('¡Ahora puedes desafiarlo en combate desde el menú principal! >:)\n')

        elif opcion == '0':
            print(f'\n¡Gracias por usar el Pokédex, {nombre_usuario}! ¡Vuelve pronto! :D\n')
            break

        else:
            print('Ups. Parece que aún no existe esa opción. T-T\n'
                  '¿Qué te parece si lo intentas una de nuestro menú? :D\n')


main()