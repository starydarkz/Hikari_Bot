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
