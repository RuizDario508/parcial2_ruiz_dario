# Parcial 2 - Sistema de Gestión de Alumnos

Sistema completo Django con autenticación, gestión de alumnos, generación de PDFs y scraping web.

## 🚀 Características

### 1. **Autenticación de Usuarios**
- ✅ Registro con username, email y password
- ✅ Login y Logout
- ✅ Envío de email de bienvenida al registrarse
- ✅ Templates con Bootstrap 5

### 2. **Dashboard de Alumnos**
- ✅ Protegido con autenticación (@login_required)
- ✅ Modelo Alumno con 3 campos: nombre, edad, curso
- ✅ CRUD completo (Crear, Ver, Editar, Eliminar)
- ✅ Cada usuario solo ve sus propios alumnos

### 3. **Generación de PDFs**
- ✅ Botón "Enviar PDF por correo" en cada alumno
- ✅ Generación de PDF con ReportLab
- ✅ Envío automático por email

### 4. **Scraping Web**
- ✅ Formulario para ingresar palabra clave
- ✅ Scraping de Wikipedia según la búsqueda
- ✅ Resultados mostrados en tabla
- ✅ Envío de resultados por email

### 5. **Deployment en Render**
- ✅ Configuración para producción
- ✅ WhiteNoise para archivos estáticos
- ✅ PostgreSQL en producción
- ✅ Variables de entorno configuradas

## 📋 Requisitos

- Python 3.11
- pip
- virtualenv (recomendado)

## 🛠️ Instalación Local

1. **Clonar el repositorio**
```bash
cd PARCIAL2\ PROGRAMACION
```

2. **Crear y activar entorno virtual**
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**
Crear archivo `.env` basado en `.env.example` (opcional para desarrollo local)

5. **Ejecutar migraciones**
```bash
python manage.py migrate
```

6. **Crear superusuario (opcional)**
```bash
python manage.py createsuperuser
```

7. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

8. **Acceder a la aplicación**
Abrir navegador en: `http://127.0.0.1:8000/`

## 🌐 Deployment en Render

### Paso 1: Preparar el repositorio
1. Asegurarse de que todos los archivos de configuración estén presentes:
   - `requirements.txt`
   - `build.sh`
   - `Procfile`
   - `runtime.txt`

### Paso 2: Crear servicio en Render
1. Ir a [Render.com](https://render.com) y crear cuenta
2. Crear nuevo **Web Service**
3. Conectar repositorio de GitHub
4. Configurar:
   - **Name**: parcial2-alumnos (o el nombre que prefieras)
   - **Environment**: Python 3
   - **Build Command**: `bash build.sh`
   - **Start Command**: `gunicorn parcial2.wsgi:application`

### Paso 3: Agregar PostgreSQL
1. En Render, crear nueva **PostgreSQL Database**
2. Copiar la URL de conexión (Internal Database URL)

### Paso 4: Variables de Entorno
Agregar las siguientes variables de entorno en Render:

```
SECRET_KEY=tu-clave-secreta-muy-larga-y-aleatoria
DEBUG=False
ALLOWED_HOSTS=tu-app.onrender.com
DATABASE_URL=(se configura automáticamente al conectar PostgreSQL)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-app-password-de-gmail
```

### Paso 5: Deploy
1. Click en **Create Web Service**
2. Esperar que el build termine
3. Acceder a tu aplicación en la URL provista por Render

## 📧 Configuración de Email

Para Gmail:
1. Habilitar **verificación en 2 pasos** en tu cuenta de Google
2. Generar **contraseña de aplicación** en: https://myaccount.google.com/apppasswords
3. Usar esa contraseña en `EMAIL_HOST_PASSWORD`

## 🗂️ Estructura del Proyecto

```
PARCIAL2 PROGRAMACION/
├── accounts/              # App de autenticación
│   ├── forms.py          # Formulario de registro
│   ├── views.py          # Vistas de login/signup
│   └── urls.py           # URLs de autenticación
├── alumnos/              # App de gestión de alumnos
│   ├── models.py         # Modelo Alumno
│   ├── forms.py          # Formulario de Alumno
│   ├── views.py          # CRUD de alumnos + PDF
│   └── urls.py           # URLs de alumnos
├── scraper/              # App de scraping
│   ├── forms.py          # Formulario de búsqueda
│   ├── views.py          # Lógica de scraping
│   └── urls.py           # URLs del scraper
├── templates/            # Templates HTML
│   ├── base.html         # Template base
│   ├── home.html         # Página principal
│   ├── accounts/         # Templates de autenticación
│   ├── alumnos/          # Templates de alumnos
│   └── scraper/          # Templates de scraper
├── parcial2/             # Configuración del proyecto
│   ├── settings.py       # Configuración principal
│   ├── urls.py           # URLs principales
│   └── wsgi.py           # WSGI para deployment
├── requirements.txt      # Dependencias Python
├── build.sh             # Script de build para Render
├── Procfile             # Comando de inicio para Render
└── runtime.txt          # Versión de Python
```

## 🎯 Uso

### Registro y Login
1. Ir a `/accounts/signup/` para registrarse
2. Recibirás un email de bienvenida
3. Hacer login en `/accounts/login/`

### Gestión de Alumnos
1. Desde el dashboard, click en "Entrar"
2. Crear nuevos alumnos con el botón "+ Agregar Alumno"
3. Ver detalles de cada alumno
4. Enviar PDF por email desde la vista de detalles
5. Editar o eliminar alumnos

### Scraping
1. Desde el dashboard, click en "Scraper"
2. Ingresar palabra clave (ej: "Python", "Django", "Educación")
3. Ver resultados en tabla
4. Recibir resultados por email automáticamente

## 📦 Dependencias Principales

- **Django 5.0.6**: Framework web
- **BeautifulSoup4**: Para scraping web
- **ReportLab**: Generación de PDFs
- **Requests**: Peticiones HTTP para scraping
- **PostgreSQL** (psycopg2-binary): Base de datos en producción
- **Gunicorn**: Servidor WSGI para producción
- **WhiteNoise**: Servir archivos estáticos en producción

## 🔒 Seguridad

- Las contraseñas se hashean automáticamente con Django
- CSRF protection habilitado
- Variables sensibles en variables de entorno
- DEBUG=False en producción
- Secret key randomizada

## 👨‍💻 Desarrollo

Para agregar nuevas funcionalidades:

1. Crear migraciones después de modificar modelos:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Ejecutar tests:
```bash
python manage.py test
```

3. Crear superusuario para admin:
```bash
python manage.py createsuperuser
```

## 📝 Notas

- El scraper usa Wikipedia en español por defecto
- Los PDFs se generan en formato simple con ReportLab
- Los emails se envían vía SMTP de Gmail
- En desarrollo, se usa SQLite
- En producción, se usa PostgreSQL

## 🐛 Troubleshooting

**Error de email:**
- Verificar que la contraseña de aplicación de Gmail sea correcta
- Verificar que la verificación en 2 pasos esté habilitada

**Error de base de datos en Render:**
- Verificar que DATABASE_URL esté configurada
- Verificar que las migraciones se ejecutaron en build.sh

**Error 404 en archivos estáticos:**
- Ejecutar `python manage.py collectstatic`
- Verificar STATIC_ROOT en settings.py

## 📞 Soporte

Para problemas o preguntas sobre el proyecto, revisar el código o contactar al desarrollador.

---
**Proyecto Parcial 2 - Programación**
