from nia_ai import obtener_respuesta

print(">>")

while True:
    prompt = input("Tú: ")
    if prompt.lower() in ["salir", "exit", "quit"]:
        print("Nia: …b-bye… vuelve pronto, ¿sí?")
        break
    respuesta = obtener_respuesta(prompt)
    print(f"Nia: {respuesta}\n")
