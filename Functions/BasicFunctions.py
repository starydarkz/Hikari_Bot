def config():
    """Configuracion del bot"""
    token = input("Escribe el token: ")
    return token
def definiciones(palabra):
    ''' Busquedas de definiciones en wikipedia '''
      
    from Resources.definiciones import definiciones
    if palabra in definiciones.keys():
        return definiciones[palabra]
    else:
        import wikipedia
        wikipedia.set_lang("es")
     
        try: 
            resumen = wikipedia.summary(palabra, sentences = 1)
            url = (wikipedia.page(palabra).url)
            resultado = (resumen + "\n\nMas info: " + url)
            return resultado
        except: 
            error =  ("No se ha encontrado esta definicion...")
            return error
