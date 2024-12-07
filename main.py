dicc = {
    "CHEPO": "Algo que alguien hace sin intencion de hacerlo"
    "LOL": "Una expresion que dice que algo da mucha risa"
    "ROFL": "Una expresion en ingles que dice que algo da mucha risa"
    "CRINGE": "La expresion que se usa para describir algo raro o penoso"
}
word = input("Escribe una palabra que no entiendas(Con mayusculas!):")
if word in dicc.keys():
    print(word, "significa", dicc.keys[word])
else:
    print("esa palabra no esta en mi diccionario, lo siento :c")
