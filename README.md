# Turnia

Turnia es una aplicación pensada para la gestión de citas y clientes. El objetivo son jóvenes autónomos que acaban de empezar y no quieren gastar mucho dinero en una gran aplicación. 

Para ello, una de las máximas es que sea simple, secilla y práctica.

---

## 🧠 Idea y objetivo

* **Problema:** Algunos jóvenes que abren pequeños negocios (peluqueros, estilistas, tatuadores...) no usan una agenda online por ser, caras o complejas.
* **Solución:** Una aplicación que les permita gestionar su tiempo de forma simple y económica es justo lo que buscan.
* **Usuario objetivo:** Autónomos de pequeña empresa jóvenes que quieren empezar a trabajar por su cuenta.

---

## 🛠️ Stack tecnológico

### Backend

* Lenguaje: Python
* Framework: Django, Django Rest Framework
* Base de datos: PostgreSQL
* Autenticación:
* Otras herramientas:

### Frontend (si aplica)

* Framework: React
* Librerías principales:

---

## 🗂️ Estructura del proyecto

```text
project-root/
├── backend/
│   ├── apps/
│   ├── config/
│   ├── requirements.txt
│   └── manage.py
├── frontend/
└── README.md
```

- **backend/**: Contiene la lógica del servidor, la API y la gestión de datos.
  - **apps/**: Aplicaciones Django que encapsulan la lógica de negocio del proyecto.
  - **config/**: Configuración global del proyecto (settings, urls, wsgi/asgi).
  - **requirements.txt**: Dependencias del backend.
  - **manage.py**: Punto de entrada para comandos de Django.

- **frontend/**: Aplicación cliente desarrollada en React. Gestiona la interfaz de usuario y la comunicación con la API.

- **README.md**: Documento principal con la descripción, instalación y uso del proyecto.

---

## ⚙️ Instalación y configuración

### Requisitos

* Python X.X
* Node.js X.X
* PostgreSQL / SQLite / etc.

### Variables de entorno

Crea un archivo `.env` con las siguientes variables:

```env
DEBUG=
SECRET_KEY=
DATABASE_URL=
```

### Instalación

```bash
# Backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend
npm install
```

---

## ▶️ Ejecución del proyecto

```bash
# Backend
python manage.py runserver

# Frontend
npm run dev
```

---

## 🧩 Funcionalidades principales

* [ ] Autenticación de usuarios
* [ ] CRUD de entidades principales
* [ ] Permisos y roles
* [ ] API REST

---

## 🧪 Testing

* Tipo de tests:
* Herramientas:

```bash
pytest
```

---

## 📐 Decisiones técnicas

Describe aquí decisiones importantes:

* Por qué elegiste este framework:

    He elegido Django porque me parece el framework más versátil para empezar una aplicación simple y luego poder ir escalándola.
* Patrones usados (MVC, Clean Architecture, etc.)
* Problemas encontrados y soluciones

---

## 🚀 Roadmap

* [ ] Feature 1
* [ ] Feature 2
* [ ] Mejoras de rendimiento

---

## 📸 Capturas (opcional)

Inserta imágenes del proyecto en funcionamiento.

---

## 📚 Aprendizajes

Qué has aprendido desarrollando este proyecto.

---

## 👤 Autor

* Nombre: Juan A. Santa León
* GitHub: https://github.com/juanandev-lab/tunia.git
* LinkedIn: www.linkedin.com/in/juan-antonio-santa-león-29392b346

---

## 📄 Licencia

Indica la licencia del proyecto (MIT, GPL, etc.).
