

def definiciones(palabra):
    """ Definiciones de palabras """
    
    from Resources.DataBase import definiciones
    
    if palabra.lower() in definiciones.keys(): # Buscamos en el diccionario  
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

def saludo():
    from Resources.DataBase import saludo
    from random import choice
    return choice(saludo)
