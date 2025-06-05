puntaje = 0

respuesta = input("1. ¿Cuál es la capital de Francia? ")
if respuesta.strip().lower() in ["parís", "paris"]:
    puntaje += 1

respuesta = input("2. ¿Cuánto es 5 multiplicado por 6? ")
if respuesta.strip() == "30":
    puntaje += 1

respuesta = input("3. ¿Cómo se dice 'gato' en inglés? ")
if respuesta.strip().lower() == "cat":
    puntaje += 1

print(f"Puntaje final: {puntaje} de 3")
