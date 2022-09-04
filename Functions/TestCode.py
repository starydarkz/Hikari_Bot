
def test(codigo):
    from os import system
    # Guardamos el codigo
    system(f"echo '{codigo}' > temp.py")
    ejecucion = os.system("python3 temp.py")
    if ejecucion==0:
        print(type(ejecucion), ejecucion)
        return "Ejecucion exitosa"
    else:
        return "Error en la ejecución"

if __name__ == '__main__':
    test('print("Hola")')
