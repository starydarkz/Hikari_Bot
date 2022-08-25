# -*- coding: utf-8 -*-

import os

#files = os.listdir()
script = os.environ["SCRIPT"]
if not os.path.exists("./output"):
    os.system("mkdir output")
ejecucion = os.system(f"python3 {script}.py | tee ./output/{script}.txt")
with open(f'./output/{script}.txt') as f:
    retorno = f.read()
    
#os.system(f"rm -r {files[0]}.txt {files[0]}.py")
if ejecucion==0:
    print(f"Felicidades tu salida es: {retorno}")
else:
    print("Error en la ejecución")