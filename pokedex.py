
class Pokemon:
    nombre = 'Sin Pokémon'
    descripcion = 'No descripción'
    ataque = 0
    defensa = 0
    vida = 0
    nivel = 0
    evolucion = 1
    atrapado = False

    '''
    def __init__(self, nombre, descripcion, ataque, defensa, vida, nivel=1, evolucion=1, atrapado=False):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.nivel = nivel
        self.evolucion = evolucion
        self.atrapado = atrapado'''
    
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

