# ✅ CHECKLIST DE VERIFICACIÓN - PARCIAL 2

Usa este checklist para verificar que el proyecto esté completo antes de entregar.

## 📋 1. AUTENTICACIÓN (25 puntos)

### Registro
- [ ] Formulario con username, email y password funciona
- [ ] Se envía email de bienvenida al registrarse
- [ ] Email se recibe correctamente
- [ ] Usuario puede iniciar sesión después de registrarse
- [ ] Template usa Bootstrap correctamente

### Login/Logout
- [ ] Login funciona con username y password
- [ ] Logout funciona y redirige correctamente
- [ ] Mensajes de error se muestran correctamente
- [ ] Usuario no autenticado no puede acceder a páginas protegidas
- [ ] Navbar muestra información del usuario logueado

**Puntos obtenidos: ___/25**

---

## 📋 2. DASHBOARD DE ALUMNOS (25 puntos)

### Modelo Alumno
- [ ] Modelo tiene al menos 3 campos (nombre, edad, curso)
- [ ] Tiene ForeignKey a User
- [ ] Tiene campo created_at

### Protección de Acceso
- [ ] Solo usuarios autenticados pueden acceder
- [ ] Cada usuario solo ve sus propios alumnos
- [ ] No se pueden ver alumnos de otros usuarios

### CRUD Completo
- [ ] **Create**: Formulario para crear alumnos funciona
- [ ] **Read**: Lista de alumnos se muestra correctamente
- [ ] **Read**: Vista de detalle muestra toda la información
- [ ] **Update**: Formulario para editar alumnos funciona
- [ ] **Delete**: Confirmación de eliminación funciona
- [ ] **Delete**: Alumno se elimina correctamente

### UI/UX
- [ ] Templates usan Bootstrap
- [ ] Formularios tienen estilos consistentes
- [ ] Navegación es intuitiva
- [ ] Hay botones para todas las acciones

**Puntos obtenidos: ___/25**

---

## 📋 3. GENERACIÓN DE PDFs (20 puntos)

### Generación
- [ ] Cada alumno tiene botón "Enviar PDF"
- [ ] PDF se genera con ReportLab
- [ ] PDF contiene nombre del alumno
- [ ] PDF contiene edad del alumno
- [ ] PDF contiene curso del alumno
- [ ] PDF tiene formato profesional

### Envío por Email
- [ ] PDF se envía por email correctamente
- [ ] Email llega a la bandeja de entrada del usuario
- [ ] PDF está adjunto al email correctamente
- [ ] Se muestra confirmación de envío exitoso
- [ ] No hay errores en la consola

**Puntos obtenidos: ___/20**

---

## 📋 4. SCRAPING WEB (15 puntos)

### Formulario
- [ ] Hay página para el scraper
- [ ] Formulario para ingresar palabra clave funciona
- [ ] Validación de formulario está activa

### Scraping
- [ ] Scraper funciona con diferentes palabras clave
- [ ] Se obtienen resultados de Wikipedia
- [ ] Manejo de errores funciona (palabras sin resultados)
- [ ] No hay crashes con palabras inválidas

### Resultados
- [ ] Resultados se muestran en tabla
- [ ] Tabla tiene headers claros
- [ ] Al menos 3 columnas de información
- [ ] Resultados son legibles y formateados

### Email
- [ ] Resultados se envían por email
- [ ] Email contiene todos los resultados
- [ ] Formato del email es legible
- [ ] Confirmación de envío se muestra

**Puntos obtenidos: ___/15**

---

## 📋 5. DEPLOYMENT EN RENDER (15 puntos)

### Archivos de Configuración
- [ ] `requirements.txt` existe y tiene todas las dependencias
- [ ] `build.sh` existe y tiene comandos correctos
- [ ] `Procfile` existe con comando de gunicorn
- [ ] `runtime.txt` especifica Python 3.11
- [ ] `.gitignore` excluye archivos sensibles
- [ ] `.env.example` tiene todas las variables necesarias

### Settings.py
- [ ] SECRET_KEY usa variable de entorno
- [ ] DEBUG usa variable de entorno
- [ ] ALLOWED_HOSTS usa variable de entorno
- [ ] DATABASE_URL está configurado
- [ ] WhiteNoise middleware está agregado
- [ ] STATIC_ROOT está configurado
- [ ] Email usa variables de entorno

### Documentación
- [ ] README.md explica el proyecto
- [ ] Instrucciones de instalación están claras
- [ ] Instrucciones de deployment están incluidas
- [ ] Estructura del proyecto está documentada

**Puntos obtenidos: ___/15**

---

## 📋 EXTRAS (Opcional)

### Bonus Points
- [ ] Diseño muy atractivo (más allá de Bootstrap básico)
- [ ] Validaciones extra en formularios
- [ ] Mensajes de éxito/error con django.contrib.messages
- [ ] Tests unitarios implementados
- [ ] Código muy bien comentado
- [ ] README con imágenes/screenshots
- [ ] Animaciones o transiciones CSS
- [ ] Favicon personalizado
- [ ] Página 404 personalizada

---

## 🧪 TESTING MANUAL

### Test de Flujo Completo

1. **Registro y Login**
```
[ ] Registrar nuevo usuario
[ ] Verificar recepción de email de bienvenida
[ ] Hacer logout
[ ] Hacer login con las credenciales creadas
```

2. **Gestión de Alumnos**
```
[ ] Crear 3 alumnos diferentes
[ ] Ver lista de alumnos
[ ] Ver detalle de cada alumno
[ ] Editar un alumno
[ ] Eliminar un alumno (con confirmación)
```

3. **PDFs**
```
[ ] Generar PDF de un alumno
[ ] Verificar recepción del email
[ ] Abrir y verificar contenido del PDF adjunto
```

4. **Scraper**
```
[ ] Buscar "Python"
[ ] Verificar resultados en tabla
[ ] Verificar recepción de email con resultados
[ ] Buscar "Django"
[ ] Buscar palabra inexistente (verificar manejo de error)
```

5. **Seguridad**
```
[ ] Intentar acceder a /alumnos/ sin login (debe redirigir)
[ ] Crear alumno con usuario A
[ ] Intentar ver alumno de usuario A logueado como usuario B
```

---

## 🚀 PRE-ENTREGA

### Archivos a Verificar Antes de Entregar

```
[ ] requirements.txt completo
[ ] README.md actualizado
[ ] DEPLOYMENT.md con instrucciones claras
[ ] .gitignore configurado
[ ] .env.example presente
[ ] Código comentado en secciones complejas
[ ] No hay archivos sensibles (.env, db.sqlite3) en Git
[ ] Migraciones generadas y aplicadas
```

### Comandos de Verificación Final

```bash
# 1. Verificar que todas las dependencias estén instaladas
pip install -r requirements-dev.txt

# 2. Verificar que no hay errores de sintaxis
python manage.py check

# 3. Verificar migraciones
python manage.py showmigrations

# 4. Ejecutar tests (si los hay)
python manage.py test

# 5. Verificar que el servidor corre sin errores
python manage.py runserver
```

### URLs a Probar

```
[ ] http://127.0.0.1:8000/ (Home)
[ ] http://127.0.0.1:8000/accounts/signup/ (Registro)
[ ] http://127.0.0.1:8000/accounts/login/ (Login)
[ ] http://127.0.0.1:8000/alumnos/ (Lista alumnos)
[ ] http://127.0.0.1:8000/alumnos/crear/ (Crear alumno)
[ ] http://127.0.0.1:8000/scraper/ (Scraper)
[ ] http://127.0.0.1:8000/admin/ (Admin)
```

---

## 📊 PUNTUACIÓN TOTAL

| Sección | Puntos Máximos | Puntos Obtenidos |
|---------|----------------|------------------|
| 1. Autenticación | 25 | ___ |
| 2. Dashboard Alumnos | 25 | ___ |
| 3. Generación PDFs | 20 | ___ |
| 4. Scraping Web | 15 | ___ |
| 5. Deployment | 15 | ___ |
| **TOTAL** | **100** | **___** |
| Extras (Bonus) | +10 | ___ |

---

## ✅ APROBACIÓN FINAL

- [ ] **Proyecto tiene puntaje >= 70**
- [ ] **Todas las funcionalidades core funcionan**
- [ ] **Código está limpio y organizado**
- [ ] **Documentación está completa**
- [ ] **Proyecto está listo para presentar**

---

## 📝 NOTAS ADICIONALES

Usa este espacio para anotar cualquier problema encontrado o mejora pendiente:

```
_________________________________________________________

_________________________________________________________

_________________________________________________________

_________________________________________________________
```

---

**Firma del Revisor: ________________   Fecha: ___/___/___**

**PROYECTO APROBADO: ☐ SÍ  ☐ NO  ☐ CON CORRECCIONES**
