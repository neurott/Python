import random

# Datos de los Pokémon
pikachu = {
    "nombre": "Pikachu",
    "vida": 100,
    "ataques": {
        "Impactrueno": 20,
        "Cola de Hierro": 15,
        "Ataque Rápido": 10,
        "Trueno": 25
    }
}

charizard = {
    "nombre": "Charizard",
    "vida": 120,
    "ataques": {
        "Lanzallamas": 25,
        "Ataque Ala": 15,
        "Garra Dragón": 20,
        "Corte": 10
    }
}

# Función para mostrar los ataques disponibles
def mostrar_ataques(pokemon):
    print(f"\nAtaques disponibles de {pokemon['nombre']}:")
    for ataque, daño in pokemon["ataques"].items():
        print(f"{ataque} (Daño: {daño})")

# Función para que el Pokémon ataque
def atacar(atacante, defensor, ataque):
    if ataque in atacante["ataques"]:
        daño = atacante["ataques"][ataque]
        defensor["vida"] -= daño
        print(f"\n{atacante['nombre']} usa {ataque}. ¡Hace {daño} puntos de daño!")
        print(f"La vida restante de {defensor['nombre']} es {defensor['vida']}.")
        if defensor["vida"] <= 0:
            print(f"\n¡{defensor['nombre']} ha sido derrotado!")
            return True
    else:
        print("\nAtaque no válido. Pierdes el turno.")
    return False

# Función para elegir ataque aleatorio del Pokémon enemigo
def ataque_enemigo(atacante, defensor):
    ataque = random.choice(list(atacante["ataques"].keys()))
    return atacar(atacante, defensor, ataque)

# Batalla Pokémon
def batalla():
    print("¡Comienza la batalla entre Pikachu y Charizard!\n")
    while pikachu["vida"] > 0 and charizard["vida"] > 0:
        print("\n--- Turno de Pikachu ---")
        mostrar_ataques(pikachu)
        ataque_elegido = input("Elige un ataque: ")
        if atacar(pikachu, charizard, ataque_elegido):
            break
        
        print("\n--- Turno de Charizard ---")
        if ataque_enemigo(charizard, pikachu):
            break
    
    # Resultado final
    print("\n--- Fin de la batalla ---")
    if pikachu["vida"] > charizard["vida"]:
        print("¡Pikachu gana la batalla!")
    elif charizard["vida"] > pikachu["vida"]:
        print("¡Charizard gana la batalla!")
    else:
        print("¡Es un empate!")

# Llamar a la función principal
batalla()
