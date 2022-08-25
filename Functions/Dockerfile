FROM python:3.7-alpine
MAINTAINER AprenderPython
LABEL version="1.0"
LABEL descripcion="Contenedor dedicado a la ejecución de los scripts de los retos de la Comunidad AprenderPython."
#USER hikari
WORKDIR /usr/src/app
RUN mkdir /work
COPY Resolvedor.py /work
CMD ["python3", "/work/Resolvedor.py"]
