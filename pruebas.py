
class Pokemon:
    nombre = 'Sin Pokémon'
    descripcion = 'No descripción'
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
        print(f'Nombre: {self.nombre}\nDescripción: {self.descripcion}\nAtaque: {self.ataque}\nDefensa: {self.defensa}\nVida: {self.vida}\nNivel: {self.nivel}\nEvolución: {self.evolucion}\nAtrapado: {self.atrapado}')

    def hablar(self):
        print(f"Pokemon dice: '¡{self.nombre}!\n'.")

    def entrenar(self):
        self.ataque += 10
        self.defensa += 10
        self.vida += 10
        self.nivel += 20

        if self.nivel >= 100:
            self.evolucion += 1
            print(f'¡{self.nombre} ha evolucionado a nivel {self.evolucion}!\n')
            self.nivel = 0
    
    def subirAtaque(self, boostAtaque):
        self.ataque += boostAtaque

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
        super().actualizar(boostAtaque + 5, boostDefensa + 5, boostVida + 5)        #? De momento no tengo muy claro si a esto se refería con sobreescribir el método actualizar
                                                                                    #? o si debía crear atributos boost específicos para cada subclase. Por ahora lo dejo así.

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


PEnemigos = []                                                                      #* Lista para almacenar los Pokémon enemigos

PEnemigo = Agua('Squirtle', 'Es una tortuga :D', 240, 325, 220, 260)
PEnemigos.append(PEnemigo)
PEnemigo = Hierba('Bulbasaur', 'Es una planta :D', 245, 245, 225, 325)
PEnemigos.append(PEnemigo)
PEnemigo = Fuego('Charmander', 'Es un lagarto :D', 260, 215, 195, 300)
PEnemigos.append(PEnemigo)
PEnemigo = Electrico('Pikachu', 'Es un ratón :D', 275, 200, 175, 250)
PEnemigos.append(PEnemigo)