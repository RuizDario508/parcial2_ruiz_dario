# 🛠️ Comandos Útiles - Proyecto Parcial 2

## 🚀 Comandos de Inicio Rápido

### Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```

### Crear superusuario para admin
```bash
python manage.py createsuperuser
```

## 🗄️ Base de Datos

### Crear migraciones
```bash
python manage.py makemigrations
```

### Aplicar migraciones
```bash
python manage.py migrate
```

### Resetear base de datos (desarrollo)
```bash
# Eliminar base de datos
del db.sqlite3

# Recrear y aplicar migraciones
python manage.py migrate

# Crear superusuario nuevamente
python manage.py createsuperuser
```

## 📦 Dependencias

### Instalar dependencias de desarrollo
```bash
pip install -r requirements-dev.txt
pip install dj-database-url whitenoise
```

### Instalar dependencias de producción
```bash
pip install -r requirements.txt
```

### Actualizar requirements.txt
```bash
pip freeze > requirements.txt
```

## 🎨 Archivos Estáticos

### Recolectar archivos estáticos
```bash
python manage.py collectstatic --no-input
```

### Limpiar archivos estáticos
```bash
# Windows
rmdir /s /q staticfiles

# Linux/Mac
rm -rf staticfiles
```

## 🧪 Testing

### Ejecutar todos los tests
```bash
python manage.py test
```

### Ejecutar tests de una app específica
```bash
python manage.py test alumnos
python manage.py test accounts
python manage.py test scraper
```

### Ejecutar test específico
```bash
python manage.py test alumnos.tests.TestAlumnoModel
```

## 🐛 Debug

### Ejecutar shell de Django
```bash
python manage.py shell
```

### Ver logs en tiempo real
```bash
python manage.py runserver --verbosity 2
```

### Verificar configuración del proyecto
```bash
python manage.py check
```

### Ver todas las URLs disponibles
```bash
python manage.py show_urls  # requiere django-extensions
```

## 📧 Email Testing

### Cambiar backend a console (para desarrollo)
En `settings.py`, cambiar temporalmente:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### Probar envío de email desde shell
```python
python manage.py shell

from django.core.mail import send_mail

send_mail(
    'Test Subject',
    'Test Message',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```

## 🔐 Seguridad

### Generar nueva SECRET_KEY
```python
python manage.py shell

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Verificar seguridad del proyecto
```bash
python manage.py check --deploy
```

## 📊 Datos de Prueba

### Crear datos de prueba (ejemplo)
```python
python manage.py shell

from django.contrib.auth.models import  User
from alumnos.models import Alumno

# Crear usuario de prueba
user = User.objects.create_user('test', 'test@example.com', 'password123')

# Crear alumnos de prueba
Alumno.objects.create(usuario=user, nombre='Juan Pérez', edad=18, curso='5to año')
Alumno.objects.create(usuario=user, nombre='María García', edad=17, curso='4to año')
Alumno.objects.create(usuario=user, nombre='Pedro López', edad=19, curso='6to año')
```

### Eliminar todos los alumnos
```python
python manage.py shell

from alumnos.models import Alumno
Alumno.objects.all().delete()
```

## 🌐 Git Commands

### Inicializar repositorio
```bash
git init
git add .
git commit -m "Initial commit - Proyecto Parcial 2"
```

### Conectar a GitHub
```bash
git remote add origin https://github.com/tu-usuario/parcial2-programacion.git
git branch -M main
git push -u origin main
```

### Actualizar repositorio
```bash
git add .
git commit -m "Descripción de cambios"
git push
```

### Ver estado
```bash
git status
```

### Ver historial
```bash
git log --oneline
```

## 🔄 Render Deployment

### Forzar nuevo deploy
```bash
# Push cualquier cambio a GitHub
git commit --allow-empty -m "Force deploy"
git push
```

### Ver logs de Render (desde dashboard)
```bash
# En Render -> Tu servicio -> Logs
```

## 🧹 Limpieza

### Eliminar archivos Python compilados
```bash
# Windows
for /r %%i in (*.pyc) do del "%%i"
for /d /r %%i in (__pycache__) do @rmdir /s /q "%%i"

# Linux/Mac
find . -type f -name "*.pyc" -delete
find . -type d -name "__pycache__" -delete
```

### Eliminar migraciones (excepto __init__.py)
```bash
# Manualmente eliminar archivos en:
# alumnos/migrations/ (excepto __init__.py)
# accounts/migrations/ (excepto __init__.py)
# scraper/migrations/ (excepto __init__.py)

# Luego recrear
python manage.py makemigrations
python manage.py migrate
```

## 📱 URLs Importantes

### Desarrollo Local
- Home: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Login: http://127.0.0.1:8000/accounts/login/
- Signup: http://127.0.0.1:8000/accounts/signup/
- Alumnos: http://127.0.0.1:8000/alumnos/
- Scraper: http://127.0.0.1:8000/scraper/

### Producción (reemplazar tu-app)
- Home: https://tu-app.onrender.com/
- Admin: https://tu-app.onrender.com/admin/
- Login: https://tu-app.onrender.com/accounts/login/
- Signup: https://tu-app.onrender.com/accounts/signup/
- Alumnos: https://tu-app.onrender.com/alumnos/
- Scraper: https://tu-app.onrender.com/scraper/

## 🎯 Troubleshooting Rápido

### Error: "No module named X"
```bash
pip install -r requirements-dev.txt
pip install dj-database-url whitenoise
```

### Error: "Table doesn't exist"
```bash
python manage.py migrate
```

### Error: "Port already in use"
```bash
# Cambiar el puerto
python manage.py runserver 8080

# O matar el proceso en puerto 8000
# Windows: netstat -ano | findstr :8000
# Luego: taskkill /PID <PID> /F
```

### Error: "CSRF verification failed"
```bash
# Limpiar cookies del navegador
# O usar modo incógnito
```

### Error de email: "SMTPAuthenticationError"
```bash
# Verificar:
# 1. Verificación en 2 pasos habilitada
# 2. Contraseña de aplicación generada
# 3. EMAIL_HOST_PASSWORD correcto en .env
```

## 💡 Tips

### Crear backup de la base de datos
```bash
# SQLite
copy db.sqlite3 db.sqlite3.backup

# PostgreSQL (en Render)
# Render hace backups automáticos
```

### Ver queries SQL ejecutadas
```python
from django.conf import settings
settings.DEBUG = True

from django.db import connection
print(connection.queries)
```

### Acceder al admin con estilo personalizado
```python
# En alumnos/admin.py
from django.contrib import admin
from .models import Alumno

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'curso', 'usuario', 'created_at')
    list_filter = ('curso', 'edad')
    search_fields = ('nombre', 'curso')
```

---

**¡Guarda este archivo para referencia rápida!** 📌
