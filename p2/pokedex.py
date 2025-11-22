import os

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

misPokemones = []


def verPokemones():
    print('\n--- Tus Pokémons Atrapados ---\n')
    j = 0
    for i in misPokemones:
        j += 1
        print(f'--------- No. {j} ---------')
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

    global nombre_usuario
    nombre_usuario = input('Por favor, ingresa tu nombre: ')
    print(fr'''¡Hola, {nombre_usuario}! :)
De momento, no tienes ningún Pokémon atrapado. :(
¡Pero el primero es cortesía de la casa! :D

Tenemos 4 tipos de Pokémon disponibles:
          1.     Agua (Squirtle)
               _,........__
            ,-'            "`-.
          ,'                   `-.
        ,'                        \
      ,'                           .
      .'\               ,"".       `
     ._.'|             / |  `       \
     |   |            `-.'  ||       `.
     |   |            '-._,'||       | \
     .`.,'             `..,'.'       , |`-.
     l                       .'`.  _/  |   `.
     `-.._'-   ,          _ _'   -" \  .     `
`."""""'-.`-...,---------','         `. `....__.
.'        `"-..___      __,'\          \  \     \
\_ .          |   `""""'    `.           . \     \
  `.          |              `.          |  .     L
    `.        |`--...________.'.        j   |     |
      `._    .'      |          `.     .|   ,     |
         `--,\       .            `7""' |  ,      |
            ` `      `            /     |  |      |    _,-'"""`-.
             \ `.     .          /      |  '      |  ,'          `.
              \  v.__  .        '       .   \    /| /              \
               \/    `""\"""""""`.       \   \  /.''                |
                `        .        `._ ___,j.  `/ .-       ,---.     |
                ,`-.      \         ."     `.  |/        j     `    |
               /    `.     \       /         \ /         |     /    j
              |       `-.   7-.._ .          |"          '         /
              |          `./_    `|          |            .     _,'
              `.           / `----|          |-............`---'
                \          \      |          |
               ,'           )     `.         |
                7____,,..--'      /          |
                                  `---.__,--.'
          2.     Fuego (Charmander)
              _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   \
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         """"'     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\
   -" /`.         _,'     | _  _  _.|
    ""--'---"""""'        `' '! |! /
                            `" " -' 
          3.     Eléctrico (Pikachu)
 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     \
        :##.       ==             .###.       `.      `.    `\
        |##:                      :###:        |        >     >
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap\
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'
                                   `:.:' 
          4.     Hierba (Bulbasaur)
                                           /
                        _,.------....___,.' ',.-.
                     ,-'          _,.--"        |
                   ,'         _.-'              .
                  /   ,     ,'                   `
                 .   /     /                     ``.
                 |  |     .                       \.\
       ____      |___._.  |       __               \ `.
     .'    `---""       ``"-.--"'`  \               .  \
    .  ,            __               `              |   .
    `,'         ,-"'  .               \             |    L
   ,'          '    _.'                -._          /    |
  ,`-.    ,".   `--'                      >.      ,'     |
 . .'\'   `-'       __    ,  ,-.         /  `.__.-      ,'
 ||:, .           ,'  ;  /  / \ `        `.    .      .'/
 j|:D  \          `--'  ' ,'_  . .         `.__, \   , /
/ L:_  |                 .  "' :_;                `.'.'
.    ""'                  """""'                    V
 `.                                 .    `.   _,..  `
   `,_   .    .                _,-'/    .. `,'   __  `
    ) \`._        ___....----"'  ,'   .'  \ |   '  \  .
   /   `. "`-.--"'         _,' ,'     `---' |    `./  |
  .   _  `""'--.._____..--"   ,             '         |
  | ." `. `-.                /-.           /          ,
  | `._.'    `,_            ;  /         ,'          .
 .'          /| `-.        . ,'         ,           ,
 '-.__ __ _,','    '`-..___;-...__   ,.'\ ____.___.'
 `"^--'..'   '-`-^-' --    `-^-'`.''"""""`.,^.`.--' ''')

    while True:
        try:
            eleccion = int(input('¿Cuál te gustaría atrapar? (Ingresa el número correspondiente): '))
        except ValueError:
                print('Ups. Parece que ese número no está dentro de las opciones. :(\n'
                      '¿Qué te parece si lo intentas de nuevo? :D\n')
        else:
            if eleccion >= 1 and eleccion <= 4:
                PDisponibles = PEnemigos
                PElegido = PDisponibles[eleccion - 1]
                PElegido.atrapado = True
                misPokemones.append(PElegido)
                os.system('cls')
                print(f'\n¡Felicidades, {nombre_usuario}! Has atrapado a {PElegido.nombre}.\n'
                      '¡Cuídalo bien y entrenen juntos para convertirse en los mejores!\n')
                break
            else:
                print('Ups. Parece que ese número no está dentro de las opciones. :(\n'
                      '¿Qué te parece si lo intentas de nuevo? :D\n')
    miPokemon = PElegido
    indice = buscarPokemon(miPokemon.nombre, True)

    print('Aquí están los detalles de tu nuevo Pokémon:\n')
    verPokemones()
    print('Qué gran aventura te espera con tu nuevo amigo. ¡Buena suerte!\n')

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
                    print(f'Opción: {op}.')

                    if op == '1':
                        misPokemones[indice].entrenar()

                    elif op == '2':
                        estadistica = input('Seleccione la estadística que desea mejorar:\n'
                                            '   -Ataque     (a)\n'
                                            '   -Defensa    (b)\n'
                                            '   -Vida       (c)\n')
                        estadistica.lower()
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
                                print('Parece que esa estadística aún no la manejo. :(\n'
                                      '¿Qué te parece si eliges otra? :D\n')
                                estadistica = input('Seleccione la estadística que desea mejorar:\n')

                    elif op == '3':
                        boost = int(input('\n¿En cuánto quiere mejorar las estadísticas de su Pokémon?: '))
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
            os.system('cls')

            import random, copy

            plantilla = random.choice(PEnemigos)
            PSalvaje = copy.deepcopy(plantilla)

            print('\n--- Combate Pokémon ---\n')
            print(f'¡Un {PSalvaje.nombre} salvaje ha aparecido! :O\n')
            PSalvaje.detallesPokemon()

            copiaMiPokemon = copy.deepcopy(misPokemones[indice])

            cargador = 0
            while True:
                os.system('cls')
                print('~~~~~~~~~~~~~~~~~~~~~~'
                      f'Defensa de {misPokemones[indice].nombre}:    {misPokemones[indice].defensa}.\n'
                      f'Vida de {misPokemones[indice].nombre}:       {misPokemones[indice].vida} ({(misPokemones[indice].vida/copiaMiPokemon.vida*100):.2f}%).\n'
                      f'Ataque normal: {misPokemones[indice].ataque}\n'
                      f'{misPokemones[indice].ataque_especial}: {misPokemones[indice].daño_especial}')
                print('~~~~~~~~~~~~~~~~~~~~~~')
                print(f'Defensa de {PSalvaje.nombre}:    {PSalvaje.defensa}.\n'
                      f'Vida de {PSalvaje.nombre}:       {PSalvaje.vida} ({(PSalvaje.vida / plantilla.vida * 100):.2f}%).\n'
                      f'Ataque normal: {PSalvaje.ataque}\n'
                      f'{PSalvaje.ataque_especial}: {PSalvaje.daño_especial}')
                print('~~~~~~~~~~~~~~~~~~~~~~')
                print('¿Qué vas a hacer ahora?\n'
                      '     1-  Pasar Turno           2-  Ataque normal\n'
                      '     3-  Ataque especial       0-  Huir')
                accion = input('Selecciona una acción: ')

                if accion == '1':
                    print(f'\n{nombre_usuario} ha decidido pasar el turno.\n')

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

                    print(
                        f'\n¡Tu {misPokemones[indice].nombre} ha atacado a {PSalvaje.nombre} salvaje con un ataque normal!\n'
                        f'Defensa de {PSalvaje.nombre}:    {PSalvaje.defensa}.\n'
                        f'Vida de {PSalvaje.nombre}:       {PSalvaje.vida} ({(PSalvaje.vida/plantilla.vida*100):.2f}%).\n')
                    cargador += 1

                elif accion == '3':
                    if cargador != 0:
                        if cargador%3 == 0:
                            if PSalvaje.defensa > 0:
                                PSalvaje.defensa -= misPokemones[indice].daño_especial
                                if PSalvaje.defensa < 0:
                                    PSalvaje.vida += PSalvaje.defensa
                                    PSalvaje.defensa = 0
                                if PSalvaje.vida < 0:
                                    PSalvaje.vida = 0

                            else:
                                PSalvaje.vida -= misPokemones[indice].daño_especial

                            if PSalvaje.vida < 0:
                                PSalvaje.vida = 0

                            print(
                                f'\n¡Tu {misPokemones[indice].nombre} ha usado {misPokemones[indice].ataque_especial} en {PSalvaje.nombre} salvaje!\n'
                                f'Defensa de {PSalvaje.nombre}:    {PSalvaje.defensa}.\n'
                                f'Vida de {PSalvaje.nombre}:       {PSalvaje.vida} ({(PSalvaje.vida/plantilla.vida*100):.2f}%).\n')
                        else:
                            print("No abuses de tus ataques especiales >:T")
                    else:
                        print("No abuses de tus ataques especiales >:T")

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
                opcionEnemigo = random.randrange(0, 9)

                if opcionEnemigo == 1 or opcionEnemigo == 2 or opcionEnemigo == 3 or opcionEnemigo == 4 or opcionEnemigo == 5 or opcionEnemigo == 6 or opcionEnemigo == 7:
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
                        f'\n¡{PSalvaje.nombre} salvaje ha atacado a tu {misPokemones[indice].nombre} con un ataque normal!\n'
                        f'Defensa de {misPokemones[indice].nombre}:    {misPokemones[indice].defensa}.\n'
                        f'Vida de {misPokemones[indice].nombre}:       {misPokemones[indice].vida} ({(misPokemones[indice].vida/copiaMiPokemon.vida*100):.2f}%).\n')

                elif opcionEnemigo == 8 or opcionEnemigo == 9:
                    if misPokemones[indice].defensa > 0:
                        misPokemones[indice].defensa -= PSalvaje.daño_especial
                        if misPokemones[indice].defensa < 0:
                            misPokemones[indice].vida += misPokemones[indice].defensa
                            misPokemones[indice].defensa = 0

                    else:
                        misPokemones[indice].vida -= PSalvaje.daño_especial
                        if misPokemones[indice].vida < 0:
                            misPokemones[indice].vida = 0

                    print(
                        f'\n¡{PSalvaje.nombre} salvaje ha usado {PSalvaje.ataque_especial} en tu {misPokemones[0].nombre}!\n'
                        f'Defensa de {misPokemones[indice].nombre}:    {misPokemones[indice].defensa}.\n'
                        f'Vida de {misPokemones[indice].nombre}:       {misPokemones[indice].vida} ({(misPokemones[indice].vida/copiaMiPokemon.vida*100):.2f}%).\n')

                elif opcionEnemigo == 0:
                    print(f'\n{PSalvaje.nombre} ha escapado del combate.\n'
                          'Creo que somos demasiado fuertes.  XD')
                    break

                else:
                    pass

                if misPokemones[indice].vida <= 0:
                    misPokemones[indice].defensa = copiaMiPokemon.defensa
                    misPokemones[indice].vida = copiaMiPokemon.vida
                    print(f'{PSalvaje.nombre} nos ha derrotado, tal vez tengamos mas suerte la próxima. TnT')
                    break

                print('~~~~~~~~~~~~~~~~~~~~~~')
            misPokemones[indice].vida = copiaMiPokemon.vida
            misPokemones[indice].defensa = copiaMiPokemon.defensa

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
                        if noPokemon > len(misPokemones):
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
                    daño_especial = int(input('Ingresa el valor del daño especial del Pokémon (1 - 1000): '))
                    if daño_especial < 1 or daño_especial > 1000:
                        print('Ups. Ese valor no está dentro del rango. :p\n')
                    else:
                        break
                except ValueError:
                    print('Introduzca la cantidad como un número entero')

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
            print(f'\n¡Gracias por usar el Pokédex, {nombre_usuario}! ¡Vuelve pronto! :D\nMe piro vampiro\n')
            break

        else:
            os.system('cls')
            print('Ups. Parece que aún no existe esa opción. T-T\n'
                  '¿Qué te parece si intentas una de nuestro menú? :D\n')

main()
