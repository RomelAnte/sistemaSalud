# 🏥 Sistema de Diagnóstico Médico - Inteligencia Artificial

Un sistema experto de diagnóstico de enfermedades comunes basado en reglas de Inteligencia Artificial desarrollado con Django y Python.

## 📋 Descripción

Este proyecto implementa un **sistema experto** que realiza diagnósticos preliminares de enfermedades comunes analizando síntomas seleccionados por el usuario. Utiliza principios básicos de IA con un motor de inferencia basado en reglas para determinar los diagnósticos más probables con niveles de confianza.

### Características Principales

- ✅ **Motor de Inferencia Basado en Reglas**: Análisis inteligente de síntomas
- ✅ **Ponderación de Confianza**: Cada diagnóstico incluye un porcentaje de confianza
- ✅ **Múltiples Diagnósticos**: Muestra los 3 diagnósticos más probables ordenados por confianza
- ✅ **Interfaz Moderna**: Diseño responsivo con gradientes y animaciones
- ✅ **Interfaz Interactiva**: Experiencia de usuario fluida con retroalimentación visual
- ✅ **Recomendaciones Médicas**: Descripción y consejos para cada diagnóstico

## 🔍 Diagnósticos Soportados

El sistema puede diagnosticar:

1. **Gripe** - Fiebre + Tos + Congestión Nasal
2. **Amigdalitis** - Fiebre + Dolor de Garganta
3. **Sarampión** - Fiebre + Erupciones
4. **Resfriado Común** - Congestión Nasal + Tos
5. **Cefalea Febril** - Dolor de Cabeza + Fiebre
6. **Alergia Respiratoria** - Congestión sin Fiebre
7. **Irritación Leve de Garganta** - Dolor de Garganta sin Fiebre

## 🛠️ Tecnología Utilizada

- **Backend**: Django 4.2 (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5.3
- **Base de Datos**: SQLite (configurada, no utilizada para datos)
- **API**: RESTful con CSRF Protection
- **IA**: Motor de Inferencia Basado en Reglas Propias

## 📁 Estructura del Proyecto

```
sistemaSalud/
├── manage.py
├── README.md
├── sistemaSalud/                  # Configuración Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── Aplicacion/
    └── ConsultaSintomas/          # App principal
        ├── migrations/
        ├── templates/
        │   ├── plantilla.html      # Template base con estilos y JavaScript
        │   ├── consultaSintomas.html # Formulario de síntomas
        │   └── diagnostico.html    # Página de resultados
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── sistema_experto.py      # Motor de inferencia
        ├── reglas.clp              # Reglas CLIPS (referencia)
        ├── urls.py
        ├── views.py
        └── tests.py
```

## 🚀 Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/usuario/sistemaSalud.git
cd sistemaSalud
```

2. **Crear entorno virtual**
```bash
python -m venv env
env\Scripts\activate  # En Windows
source env/bin/activate  # En macOS/Linux
```

3. **Instalar dependencias**
```bash
pip install django
```

4. **Aplicar migraciones**
```bash
python manage.py migrate
```

5. **Ejecutar servidor**
```bash
python manage.py runserver
```

6. **Acceder a la aplicación**
Abre tu navegador y ve a: `http://127.0.0.1:8000/`

## 📖 Cómo Usar

1. Abre la aplicación en tu navegador
2. En la página "Consulta de Síntomas", selecciona los síntomas que presentas
3. Haz clic en "Consultar Diagnóstico"
4. El sistema te mostrará los 3 diagnósticos más probables con:
   - Nombre del diagnóstico
   - Porcentaje de confianza
   - Descripción y recomendaciones

⚠️ **IMPORTANTE**: Este sistema es **informativo** y **no reemplaza** la consulta médica profesional. Siempre consulta a un profesional médico para un diagnóstico definitivo.

## 🧠 Algoritmo de Diagnóstico

El sistema utiliza un motor de inferencia que:

1. **Recibe Hechos**: Los síntomas seleccionados por el usuario
2. **Aplica Reglas**: Compara los hechos contra un conjunto de reglas predefinidas
3. **Calcula Confianza**: Cada regla tiene un nivel de confianza basado en:
   - Número de síntomas detectados
   - Relevancia de la combinación de síntomas
4. **Ordena Resultados**: Muestra los diagnósticos ordenados por confianza
5. **Devuelve Diagnósticos**: Los 3 más probables con información detallada

### Ejemplo de Regla

```python
if tiene_fiebre and tiene_tos and tiene_congestion_nasal:
    diagnostico = "Gripe" (confianza: 95%)
```

## 🔧 Módulos Principales

### `sistema_experto.py`
Contiene la función `obtener_diagnostico()` que:
- Recibe un diccionario con los síntomas
- Aplica el conjunto de reglas
- Retorna una lista de diagnósticos con confianza

### `views.py`
Controla las vistas:
- `home()`: Muestra el formulario inicial
- `diagnostico()`: Procesa el formulario y retorna los diagnósticos en JSON

### Templates
- **plantilla.html**: Base con estilos, navegación y JavaScript
- **consultaSintomas.html**: Formulario interactivo de síntomas
- **diagnostico.html**: Página de resultados

## 📊 Mejoras Futuras

- [ ] Agregar base de datos de enfermedades más amplia
- [ ] Implementar machine learning para aprendizaje automático
- [ ] Agregar historial de diagnósticos
- [ ] Sistema de recomendación de especialistas
- [ ] API pública para integración con otras aplicaciones
- [ ] Pruebas unitarias completas
- [ ] Soporte multiidioma

## 🧪 Pruebas

Para ejecutar las pruebas:
```bash
python manage.py test
```

## 📝 Licencia

Este proyecto está bajo licencia MIT. Ver archivo LICENSE para más detalles.

## 👨‍💻 Desarrollo

### Estructura de Commits

- `feat:` Nuevas características
- `fix:` Correcciones de bugs
- `docs:` Documentación
- `style:` Cambios de formato/estilo
- `refactor:` Refactorización de código

## ⚠️ Disclaimer Médico

Este sistema es una herramienta educativa y no debe ser utilizado para:
- Diagnóstico médico profesional
- Reemplazo de consulta médica
- Tratamiento autoadministrado sin supervisión

**Siempre consulte a un profesional médico calificado para diagnósticos y tratamientos.**

## 👥 Autor

Desarrollado como proyecto de IA y Django.

## 📞 Soporte

Para reportar bugs o sugerencias, crea un issue en el repositorio.

---

**Última actualización**: Junio 2026
