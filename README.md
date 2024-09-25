# 🎬 **Cinema World** 🌍

**Cinema World** es una aplicación web tipo blog, construida con el framework **Django**, que permite a los usuarios navegar por diferentes secciones como **Inicio**, **Acerca de**, **Artículos**, **Contacto**, y un **Mapa del sitio**.

## 🚀 **Características del Proyecto**

- 📑 Sistema de navegación con páginas estáticas:
  - **Inicio**
  - **Acerca de**
  - **Artículos**
  - **Contacto**
  - **Mapa del sitio**
  
- 💻 Utilización del framework **Django** para el manejo de rutas y vistas dinámicas.
- 🎨 Archivos estáticos como CSS, JS e imágenes correctamente gestionados a través del sistema de archivos estáticos de Django.
- 🔒 Configuración


##🚧 Estructura del Proyecto**

 cinema-world/
├── blog_project/                # Proyecto principal de Django
│   ├── blog/                    # Aplicación del blog
│   │   ├── templates/           # Plantillas HTML
│   │   └── static/              # Archivos estáticos (CSS, JS, imágenes)
│   ├── settings.py              # Configuraciones de Django
│   ├── urls.py                  # Configuración de rutas
│   ├── wsgi.py                  # Configuración para servidores de producción
├── static/                      # Carpeta para archivos estáticos recolectados
├── manage.py                    # Script para ejecutar comandos de Django
├── db.sqlite3                   # Base de datos SQLite (si es usada)
└── env/                         # Entorno virtual


---

# 🎬 **Cinema World** 🌍

**Cinema World** es una aplicación web tipo blog, construida con el framework **Django**, que permite a los usuarios navegar por diferentes secciones como **Inicio**, **Acerca de**, **Artículos**, **Contacto**, y un **Mapa del sitio**.

## 🚀 **Características del Proyecto**

- 📑 Sistema de navegación con páginas estáticas:
  - **Inicio**
  - **Acerca de**
  - **Artículos**
  - **Contacto**
  - **Mapa del sitio**
  
- 💻 Utilización del framework **Django** para el manejo de rutas y vistas dinámicas.
- 🎨 Archivos estáticos como CSS, JS e imágenes correctamente gestionados a través del sistema de archivos estáticos de Django.
- 🔒 Configuración preparada para despliegue en producción con archivos estáticos listos para ser servidos por **Nginx** o **Apache**.

---

## 🛠️ **Instalación y Configuración**

Sigue los pasos a continuación para configurar y ejecutar este proyecto en tu máquina local.

### 1. **Clonar el Repositorio**

Primero, clona el repositorio a tu máquina local:
git clone https://github.com/WolfWilson/informatorio_blog.git
cd blog-project


2. Crear y Activar un Entorno Virtual
python -m venv env
En Windows:
.\env\Scripts\activate

3. Instalar Dependencias
Una vez activado el entorno virtual, instala las dependencias necesarias desde el archivo requirements.txt: pip install -r requirements.txt

4. Configurar la Base de Datos
Django viene preconfigurado para usar SQLite, por lo que no necesitas instalar una base de datos adicional. Asegúrate de aplicar las migraciones para configurar la base de datos:
python manage.py migrate

5. Crear un Superusuario (opcional)
Si deseas acceder al panel de administración de Django, crea un superusuario:
python manage.py createsuperuser

6. Ejecutar el Servidor de Desarrollo
python manage.py runserver

Abre tu navegador y accede a: http://127.0.0.1:8000/
