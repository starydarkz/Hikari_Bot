# Hikari Bot
![Avatar del Bot](Logo.jpeg)

 - [Habilidades](#habilidades)
 - [Requisitos](#requisitos)
 - [Para desarrollar](#para-desarrollar)

Bot diseñado para realizar ciertas automatizaciones en el grupo de Telegram 
 - [Habilidades o Comandos que puede realizar](#habilidades)
 - [Requisitos para desarrollar](#requisitos)
## Habilidades
 - /start - Saludame y veras si estoy viva.
 - /help - Invoca este mensaje de ayuda.
 - /rules - Invoca las reglas de la comunidad.
 - /quees - Busca alguna definicion de algo.
## Requisitos:
Para el desarrollo del bot, en caso de realizar algún fork o algo parecido, debe tener en cuenta lo siguiente:
 - Python3 
 - Token de Telgram
 - Wikipedia

Para desarrollar el bot, vas a necesitar las dependencias ya mencionadas, para esto puedes ejecutar los siguientes comandos: 
> Tener Python3 instalado conjunto de PIP
```bash
pip3 install python-telegram-bot telegram wikipedia sqlite
```
## Para Desarrollar:
Si deseas colaborar en el proyecto te recomendamos las siguientes etiquitas a la hora de escribir tu commit, esto facilita la tarea a la hora de revisar las modificaciones y evitar fallos.
 - feat: La nueva característica que agregas a una aplicación en particular
 - fix: Un parche para un error
 - style: Características o actualizaciones relacionadas con estilos
 - refactor: Refactorizar una sección específica de la base de código
 - test: Todo lo relacionado con pruebas
 - docs: Todo lo relacionado con documentación
 - chore: Mantenimiento de código regular.

**Docker**
```bash
echo "MySQL"
# MySQL
docker run -v ~/personal/Hikari_Bot/basededatos/:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=hikari -p 3306:3306 --name Hikari_DB -d mysql

# EXEC
docker exec -it Hikari_DB mysql -u root -p
```

## Comunicate con Nosotros
Cualquier bug o mejora reportarlo en @AprenderPython en Telegram
