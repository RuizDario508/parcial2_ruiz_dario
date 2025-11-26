# 🚀 Guía de Deployment en Render

## Pasos para deployar el proyecto en Render.com

### 1. Preparación del Repositorio

Asegúrate de tener todos estos archivos en tu repositorio:

- ✅ `requirements.txt` - Dependencias de Python
- ✅ `build.sh` - Script de construcción
- ✅ `Procfile` - Comando para iniciar el servidor
- ✅ `runtime.txt` - Versión de Python
- ✅ `.gitignore` - Archivos a ignorar en Git

### 2. Subir el Código a GitHub

```bash
# Inicializar repositorio Git
git init

# Agregar archivos
git add .

# Crear commit
git commit -m "Proyecto Parcial 2 - Sistema de Gestión de Alumnos"

# Agregar remote (reemplaza con tu URL de GitHub)
git remote add origin https://github.com/tu-usuario/parcial2-programacion.git

# Subir código
git push -u origin main
```

### 3. Crear Servicio Web en Render

1. Ve a [Render.com](https://render.com) y crea una cuenta
2. Click en **New +** → **Web Service**
3. Conecta tu repositorio de GitHub
4. Configura el servicio:

#### Configuración Básica
- **Name**: `parcial2-alumnos` (o el nombre que prefieras)
- **Region**: Elegir región más cercana
- **Branch**: `main`
- **Root Directory**: dejar vacío
- **Runtime**: `Python 3`
- **Build Command**: `bash build.sh`
- **Start Command**: `gunicorn parcial2.wsgi:application`

#### Plan
- Seleccionar **Free Plan** (para pruebas)

### 4. Crear Base de Datos PostgreSQL

1. En Render, click en **New +** → **PostgreSQL**
2. Configura la base de datos:
   - **Name**: `parcial2-db`
   - **Database**: `parcial2`
   - **User**: se genera automáticamente
   - **Region**: la misma que tu Web Service
   - **Plan**: Free

3. **Copiar la Internal Database URL** (se usará en el siguiente paso)

### 5. Configurar Variables de Entorno

En la configuración de tu Web Service, ve a la sección **Environment** y agrega:

```
SECRET_KEY=tu-clave-secreta-super-larga-y-aleatoria-genera-una-nueva
DEBUG=False
ALLOWED_HOSTS=tu-app.onrender.com
DATABASE_URL=internal-database-url-que-copiaste-del-paso-anterior
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-contraseña-de-aplicacion-de-gmail
```

#### Generar SECRET_KEY

Puedes generar una nueva secret key en Python:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

#### Configurar Email de Gmail

1. Ir a tu cuenta de Google
2. Habilitar **Verificación en 2 pasos**
3. Ir a [App Passwords](https://myaccount.google.com/apppasswords)
4. Crear una nueva contraseña de aplicación
5. Usar esa contraseña en `EMAIL_HOST_PASSWORD`

### 6. Conectar Base de Datos al Web Service

1. En la página de tu Web Service en Render
2. Ir a la pestaña **Environment**
3. Click en **Add Environment Group**
4. Seleccionar tu base de datos PostgreSQL
5. Esto agregará automáticamente `DATABASE_URL`

### 7. Deploy

1. Click en **Create Web Service**
2. Render automáticamente:
   - Instalará dependencias
   - Ejecutará migraciones
   - Recolectará archivos estáticos
   - Iniciará el servidor

3. Ver logs en tiempo real en la pestaña **Logs**

### 8. Crear Superusuario (Opcional)

Para acceder al admin de Django:

1. Ir a la pestaña **Shell** en tu servicio
2. Ejecutar:
```bash
python manage.py createsuperuser
```

### 9. Verificar Deployment

1. Acceder a tu aplicación: `https://tu-app.onrender.com`
2. Probar:
   - ✅ Registro de usuario
   - ✅ Login
   - ✅ Creación de alumnos
   - ✅ Generación de PDFs
   - ✅ Scraping web
   - ✅ Recepción de emails

## ⚠️ Troubleshooting

### Error: "Application error"
- Revisar logs en la pestaña **Logs**
- Verificar que todas las variables de entorno estén configuradas
- Verificar que DATABASE_URL esté presente

### Error: "No module named X"
- Verificar que todas las dependencias estén en `requirements.txt`
- Forzar un nuevo deploy

### Error: "Invalid HTTP_HOST header"
- Agregar el dominio completo de Render a `ALLOWED_HOSTS`
- Ejemplo: `tu-app.onrender.com`

### Emails no se envían
- Verificar configuración de Gmail
- Revisar que la contraseña de aplicación sea correcta
- Verificar logs para errores de SMTP

### Archivos estáticos no cargan
- Verificar que `build.sh` contenga `python manage.py collectstatic --no-input`
- Verificar configuración de STORAGES en settings.py

## 🔄 Actualizaciones

Para actualizar tu aplicación después del primer deploy:

```bash
# Hacer cambios en el código
git add .
git commit -m "Descripción de cambios"
git push

# Render detectará los cambios y hará auto-deploy
```

## 📊 Monitoreo

- **Logs**: Ver en la pestaña Logs de Render
- **Metrics**: Ver uso de recursos en la pestaña Metrics
- **Events**: Ver historial de deploys en Events

## 💰 Costos

- **Free Plan**: Incluye 750 horas/mes
- La app se duerme después de 15 minutos de inactividad
- Primera request puede tomar 30-50 segundos en despertar
- Para mantenerla activa 24/7, usar un plan pago

## 🔐 Seguridad

- ✅ Nunca subir `.env` al repositorio
- ✅ Usar variables de entorno para datos sensibles
- ✅ Mantener `DEBUG=False` en producción
- ✅ Generar nueva `SECRET_KEY` para producción
- ✅ Usar contraseñas de aplicación de Gmail, no la contraseña real

## 📚 Recursos

- [Documentación de Render](https://render.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [WhiteNoise Docs](http://whitenoise.evans.io/)

---

¡Tu aplicación Django ahora está en producción! 🎉
