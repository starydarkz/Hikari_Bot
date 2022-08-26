# -*- coding: utf-8 -*-

import os
import docker

class hikari_docker():
    def __init__(self):
        self._path = "/usr/src/app/"
        self._client = docker.from_env()
        self._tags = []
        for i in self._client.images.list():
            if i.tags:
                self._tags.append(i.tags[0])

        if "hikari-test:latest" not in self._tags:
            try:
                # Lograr crear la imagen con la librería
                #self._client.images.build(target="hikari-test")
                os.system("docker build -t hikari-test .")
            except:
                print("[ERROR] - No se pudo crear la imagen.")
    
    def run_test(self, username, reto, code):
        # Guardar el código en un archivo para ejecutar dentro del contenedor
        with open(self._path + username + "-" + reto+".py", "w") as f:
            f.write(code)
        
        self.result = self._client.containers.run("hikari-test", volumes=['/usr/src/app:/usr/src/app'], environment=[f"SCRIPT={username}-{reto}"])
        
        # Eliminar los procesos residuales
        self._client.containers.prune()
