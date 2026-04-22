# Microservicios con Docker: Orquestación, Redes y Resiliencia

Este proyecto demuestra el despliegue de una arquitectura de microservicios robusta y escalable utilizando **Docker** y **Docker Compose**. La infraestructura se gestiona como código (IaC) mediante **Vagrant**, garantizando un entorno de desarrollo idéntico al de producción sobre **Pop!_OS**.



## 🚀 Descripción del Proyecto
Se ha implementado un stack tecnológico de microservicios con un fuerte enfoque en la **seguridad por segmentación de redes** y la **resiliencia operativa**. A diferencia de un despliegue básico, este proyecto implementa mecanismos de auto-recuperación y verificación de estado (Healthchecks) para garantizar la disponibilidad de los servicios.

### 🛠️ Tecnologías Utilizadas
* **Infraestructura:** Vagrant, VirtualBox (Ubuntu 22.04 LTS).
* **Orquestación:** Docker & Docker Compose V2.
* **Backend:** Python 3.9 + Flask (API REST).
* **Caché/Base de Datos:** Redis (Alpine Linux).
* **Proxy/Web:** Nginx (Reverse Proxy).
* **Observabilidad:** Portainer CE (Console de gestión visual).
* **Entorno de desarrollo:** Neovim, Tmux, Zsh.

---

## 🏗️ Arquitectura de Red y Resiliencia

### 🔐 Segmentación de Redes (Isolation)
El proyecto utiliza una estrategia de **doble red** para aislar los componentes críticos:
* **Frontend Net:** Conecta Nginx y Portainer con el tráfico externo.
* **Backend Net:** Red privada que aísla la App y Redis, protegiendo los datos sensibles y evitando que la base de datos sea expuesta a internet.



### 🩺 Healthchecks y Dependencias de Servicio
Se ha configurado una lógica de arranque inteligente para evitar fallos en cascada:
1.  **Redis Health:** Se implementó un `healthcheck` que verifica la disponibilidad del servicio mediante `redis-cli ping` cada 5 segundos.
2.  **App Resiliency:** La aplicación de Python cuenta con una dependencia condicionada (`service_healthy`). No inicia hasta que Redis confirma que está operativo.
3.  **Auto-healing:** Todos los servicios incluyen políticas de reinicio automático (`restart: always`).

---

## 📈 Fases del Proyecto

1.  **Fase 1: Infraestructura IaC:** Aprovisionamiento automatizado de la VM con Vagrant y configuración del motor Docker.
2.  **Fase 2: Redes y Almacenamiento:** Configuración de volúmenes persistentes y redes aisladas.
3.  **Fase 3: Desarrollo y Proxy Inverso:** Dockerización de la API en Python y configuración de Nginx como punto de entrada único.
4.  **Fase 4: Observabilidad:** Implementación de Portainer para el monitoreo visual de logs y gestión de contenedores.
5.  **Fase 5: Optimización de Salud:** Configuración de Healthchecks y orquestación de dependencias entre servicios.

---

## ⚙️ Cómo ejecutar este proyecto

1.  **Levantar la infraestructura:**
    ```bash
    vagrant up
    vagrant ssh
    ```
2.  **Desplegar el Stack:**
    ```bash
    cd /vagrant/docker-compose
    docker compose up -d --build
    ```

### Puertos de Acceso:
* **Aplicación Web:** Puerto 80 (vía Nginx).
* **Dashboard Portainer:** Puerto 9443 (HTTPS seguro).

---

## 👨‍💻 Autor
**Orlando** – Tecnólogo en Sistemas con más de 15 años de experiencia en IT.
*Cali, Colombia.*
