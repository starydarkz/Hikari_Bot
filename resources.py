import random

resources = {
    "saludo" : [
        "Hola Humano :)", 
        "Holaa", "Aqui estoy 👋", 
        "Hikari: On \n:b"
    ],

    "help": """
Hi, mi nombre es Hikari y aqui podras aprender a usarme :)

Los comandos disponibles son:
/start - Saludame y veras si estoy viva.
/help - Invoca este mensaje de ayuda.
/rules - Invoca las reglas de la comunidad.
/quees - Busca alguna definicion de algo.
/testcode - Probar código Python.

Create by: @aprenderpython
Code: github.com/staryzadkz/hikari_bot
    """,

    "rules": """
Objetivos del grupo:

Grupo enfocado en aprender Python practicando y resolviendo problemas desde el nivel mas básico y área relacionada con Python, retos e ideas de programas constantes para practicar y proyectos en grupo.

Reglas:

1.)No insultar a otros miembros
2.)Respetar las opiniones de los demás.
3.)No hacer spam  de offtopic.
4.)Antes de hacer una pregunta investigar.
5.)Enviar imagen o link en vez de codigo por chat.
    """,

    "test": """
Hola, si quieres enviar tu codigo por favor hazlo de la siguiente manera
/testcode 
# Vas a realizar un salto de linea
print('Hikari, :b')
    """
}

# Create a function that only return the content from the dict
def saludo():
    return random.choice(resources['saludo'])
def help():
    return resources['help']
def rules():
    return resources['rules']
def test():
    return resources['test']

if __name__ == '__main__':
    print(saludo())
