# API RESTful con Node.js, Express, Prisma y PostgreSQL

> **Autor:** David Salmeron  
> **Licencia:** Código Libre (Open Source)

Esta API sirve principalmente como entorno de prueba y demostración. Si deseas utilizarla en un entorno de producción o para un uso real, queda a tu total discreción y responsabilidad. ¡Es de código libre, por lo que cualquiera es libre de modificarla, mejorarla o hacer lo que quiera con ella! :D

---

## 📋 Requisitos Previos

Para poder clonar y ejecutar esta API en tu máquina local sin necesidad de instalar PostgreSQL ni Node.js directamente en el sistema operativo, únicamente necesitas tener instalado:

1. **Git** (para clonar el repositorio)
2. **Docker** y **Docker Compose** (para levantar la API y la base de datos de manera autocontenida)

### Instrucciones de Instalación de Requisitos

* **En Arch Linux:**
  ```bash
  sudo pacman -S git docker docker-compose
  sudo systemctl enable --now docker




  UBUNTU/DEBIAN
  sudo apt update
sudo apt install git docker.io docker-compose-v2
sudo systemctl enable --now docker



En Windows / macOS:
Instala Docker Desktop, el cual ya incluye Git Bash, Docker Engine y Docker Compose.




Clonar repositorio
git clone <URL_REPO>
cd APILM

Variables de entorno
cp .env.example .env

Levantar el contenedor docker
sudo docker compose up -d --build

sincronizar
sudo docker exec -it apilm_api npx prisma db push


Consultas
curl http://localhost:3000/productos


Crear un producto 
curl -X POST http://localhost:3000/productos \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Laptop", "precio": 1200}'


  Logs de la api
  sudo docker compose logs -f api

  Detener servicio del docker
  sudo docker compose down

