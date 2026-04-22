Microservicios con Docker: Orquestación, Redes y Observabilidad
Este proyecto demuestra el despliegue de una arquitectura de microservicios robusta y escalable utilizando Docker y Docker Compose. La infraestructura se gestiona como código mediante Vagrant, garantizando un entorno de desarrollo idéntico al de producción.

🚀 Descripción del Proyecto
Se ha implementado un stack tecnológico completo que incluye un servidor web como Proxy Inverso, una API desarrollada en Python, una base de datos NoSQL para caché y una consola de gestión visual. El enfoque principal es la seguridad por segmentación de redes y la automatización.

🛠️ Tecnologías Utilizadas
Infraestructura: Vagrant, VirtualBox (Ubuntu 22.04 LTS).

Orquestación: Docker & Docker Compose V2.

Backend: Python 3.9 + Flask.

Caché/Base de Datos: Redis (Alpine Linux).

Proxy/Web: Nginx.

Observabilidad: Portainer CE.

Editor/Terminal: Neovim, Tmux, Zsh (Pop!_OS).

🏗️ Arquitectura de Red y Servicios
El proyecto utiliza una estrategia de doble red (Dual-Network) para aislar los componentes sensibles:

Frontend Network: Conecta el Proxy Inverso (Nginx) con el mundo exterior y la consola de gestión (Portainer).

Backend Network: Una red privada donde reside la lógica de negocio (Python) y la persistencia (Redis). El mundo exterior no puede acceder directamente a Redis ni a la App de Python.

📈 Progreso del Proyecto
Fase 1: Infraestructura como Código (IaC) ✅
Automatización del aprovisionamiento de la VM con Vagrant.

Instalación automatizada del motor de Docker y Docker Compose V2.

Fase 2: Definición de Orquestación ✅
Creación del archivo docker-compose.yml base.

Configuración de volúmenes persistentes y redes aisladas.

Fase 3: Desarrollo y Proxy Inverso ✅
Desarrollo de una API en Python/Flask que interactúa con Redis.

Configuración de Nginx como Reverse Proxy, optimizando las cabeceras de tráfico y la seguridad.

Creación de imágenes personalizadas mediante Dockerfiles optimizados (imágenes slim).

Fase 4: Observabilidad y Gestión ✅
Despliegue de Portainer para el monitoreo de recursos en tiempo real.

Análisis de logs y gestión de contenedores vía GUI sobre HTTPS (Puerto 9443).

⚙️ Cómo ejecutar este proyecto
Clonar el repositorio:

Bash
git clone https://github.com/odominguezm/microservicios-docker-orchestration.git
cd microservicios-docker-orchestration
Levantar la infraestructura:

Bash
vagrant up
vagrant ssh
Desplegar el Stack:

Bash
cd /vagrant/docker-compose
docker compose up -d --build
Acceso:

App: http://localhost:8080 (o la IP asignada).

Portainer: https://localhost:9443.

👨‍💻 Autor
Orlando – Tecnólogo en Sistemas | Entusiasta de Linux y Free Software.
Cali, Colombia.
