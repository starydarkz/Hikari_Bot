import os
import random

def config():
    # Inserción del token
    return input("Escribe el token: ")

def definiciones(palabra):
    from Functions.definiciones import definiciones
    if palabra in definiciones.keys(): # Buscamos en el diccionario  
        return definiciones[palabra]
    else:
        import wikipedia # Buscamos la definicion en Wikipedia
        wikipedia.set_lang("es")
        try: 
            resumen = wikipedia.summary(palabra, sentences = 1)
            url = (wikipedia.page(palabra).url)
            return (resumen + "\n\nMas info: " + url)
        except: 
            return "No se ha encontrado esta definicion..."

def test(codigo):
    # creamos el fichero
    numero = random.random()
    os.system(f"echo '{codigo}' > {numero}.py")
    # ejecutamos el codigo y la salida se almacena en otro fichero
    ejecucion = os.system(f"python3 {numero}.py | tee ./{numero}.txt")
    # leemos el archivo
    salida = open(f'{numero}.txt')
    # eliminamos el archivo
    retorno = salida.read()
    os.system(f"rm -r {numero}.txt {numero}.py")
    if ejecucion==0:
        return ('Felicidades tu salida es: '+retorno)
    else:
        return "Error en la ejecución"

if __name__ == '__main__':
    test('print("Hola")')
