# ASY5131 python web service

Proyecto base para la creacion de pruebas unitarias

# Sobre la base de datos
Para levantar este aplicativo de ejemplo, necesitas un motor PostgresSQL.
En caso de no tener, puedes usar un contenedor Docker para levantar la base de datos sin instalar ninguna instancia en tu computador.

## Instrucciones para levantar la base de datos con docker
1. Instalar docker en tu sistema operativo
2. Correr el comando `docker compose up` en tu terminal. Este comando debe ser ejecutado en la raiz del proyecto ya que intentara leer las configuraciones del archivo `docker-compose.yaml`.

# Comandos de utilidad Aplicativo

## Levantar aplicacion
```
pip install -r requirements.txt
fastapi dev app/main.py
```

## Ejecutar pruebas
```
pytest
```

## Coverage
```
pytest --cov=app
```

# Variables de Entorno
Debes definir un archivo `.env`. A continuacion un ejemplo de su estructura

```
DATABASE_URL=
SECRET_KEY=
ALGORITHM_HASH=
DEBUG=True
```