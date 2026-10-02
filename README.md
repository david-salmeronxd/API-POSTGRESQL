# API RESTful con Node.js, Express, Prisma y PostgreSQL

> **Autor:** David Salmerón  
> **Licencia:** GNU General Public License v2.0 (GPL-2.0)

Esta API y su cliente gráfico en Python sirven como entorno de prueba y desarrollo. Es un proyecto de código abierto distribuido bajo la licencia **GPLv2**, por lo que eres libre de clonar, modificar, redistribuir y mejorar el código.

---

## 📋 Requisitos Previos

Solo necesitas **Git** y **Docker** instalados en tu sistema. No es necesario instalar Node.js ni PostgreSQL directamente en el sistema operativo.

### Instalación de Requisitos

**En Arch Linux:**

```bash
sudo pacman -S git docker docker-compose
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

**En Ubuntu / Debian:**

```bash
sudo apt update
sudo apt install -y git docker.io docker-compose-v2
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

**En Windows:**

Instala Docker Desktop y Git for Windows. Asegúrate de iniciar Docker Desktop antes de ejecutar los comandos.

## 🚀 Guía de Inicio Rápido

### 1. Clonar el repositorio

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd API-POSTGRESQL
```

### 2. Configurar variables de entorno

Crea tu archivo `.env` a partir del ejemplo:

```bash
cp .env.example .env
```

### 3. Levantar los contenedores de Docker

Este comando descargará PostgreSQL, compilará la API de Express y ejecutará las migraciones de Prisma automáticamente.

**En Linux:**

```bash
sudo docker compose up -d --build
```

**En Windows (CMD / PowerShell):**

```dos
docker compose up -d --build
```

## 🖥️ Uso de la Aplicación Gráfica (Python / Tkinter)

El proyecto incluye una interfaz gráfica para administrar el inventario de productos en tiempo real.

### Opción A: Ejecutables precompilados (Sin instalar Python)

**En Arch Linux:**

```bash
./dist/appa/appa
```

**En Windows:**

Haz doble clic en `dist/appw.exe` o ejecútalo desde CMD:

```dos
.\dist\appw.exe
```

### Opción B: Ejecutar desde el código fuente Python

Si tienes Python instalado en tu sistema:

```bash
python app.py
```

## 📡 Endpoints de la API REST

Si prefieres probar la API directamente mediante curl o Postman:

| Método | Endpoint | Descripción |
| --- | --- | --- |
| GET | `/` | Estado del servidor |
| GET | `/api/productos` | Obtener la lista completa de productos |
| POST | `/api/productos` | Crear un nuevo producto |
| DELETE | `/api/productos/:id` | Eliminar un producto por su ID |

### Ejemplos con curl

Obtener todos los productos:

```bash
curl -i http://localhost:3000/api/productos
```

Crear un nuevo producto:

```bash
curl -i -X POST http://localhost:3000/api/productos \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Teclado Mecánico", "precio": 85.50, "descripcion": "Switch Red RGB"}'
```

Eliminar un producto por ID:

```bash
curl -i -X DELETE http://localhost:3000/api/productos/1
```

## 🗄 Consultar Base de Datos desde Terminal (psql)

Para verificar las tablas directamente en la base de datos PostgreSQL:

**En Linux:**

```bash
sudo docker compose exec postgres psql -U postgres -d mi_api_db -c 'SELECT * FROM "Product";'
```

**En Windows (CMD / PowerShell):**

```dos
docker compose exec postgres psql -U postgres -d mi_api_db -c "SELECT * FROM \"Product\";"
```

## 🛠 Comandos de Mantenimiento

Ver logs del servidor en tiempo real:

```bash
docker compose logs -f api
```

Reiniciar el servidor de la API:

```bash
docker compose restart api
```

Detener todos los servicios:

```bash
docker compose down
```

## 📜 Licencia

Este proyecto está bajo la Licencia GNU General Public License v2.0 (GPLv2).

### GNU GENERAL PUBLIC LICENSE

Version 2, June 1991

Copyright (C) 2026 David Salmerón.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.