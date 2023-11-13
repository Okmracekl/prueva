no = ["n", "N", "NO", "no"]
dict = {
        "CRINGE": "Algo excepcionalmente raro o embarazoso",
        "LOL": "Una respuesta común a algo gracioso",
        "ROFL": "una respuesta a una broma",
        "SHEESH": "ligera desaprobación",
        "CREEPY": "algo aterrador o siniestro",
        "AGGRO": "ponerse agresivo/enojado"
        }
while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in dict.keys():
        print (word, ": significa o es ", dict[word])
    else:
        print("Tal vez escribiste la palabra mal, o simplemente no está en el diccionario")
    if input("Preguntar de nuevo? --> ") in no:
        break
