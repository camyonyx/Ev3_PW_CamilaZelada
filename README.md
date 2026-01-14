# Evaluación Unidad 3: Programación Web con Flask y Python

Este repositorio contiene el desarrollo de la Evaluación de la Unidad 3 de la asignatura **Programación Web**. El proyecto consiste en una aplicación web dinámica construida con el micro-framework **Flask**, que integra lógica de procesamiento de datos en el servidor y una interfaz de usuario estilizada.

## 🚀 Funcionalidades
La aplicación se divide en dos módulos principales accesibles desde un menú de inicio:

1. **Ejercicio 1 - Gestión Académica:**
   - Captura de 3 notas y porcentaje de asistencia.
   - Cálculo automático del promedio.
   - Validación lógica: Determina si el alumno está "APROBADO" (Promedio >= 4.0 y Asistencia >= 75%) o "REPROBADO".
   - Interfaz dinámica con colores de alerta (Verde/Rojo).

2. **Ejercicio 2 - Analizador de Nombres:**
   - Comparación de longitud entre tres nombres ingresados.
   - Identificación del nombre con mayor cantidad de caracteres.
   - **Gestión de Empates:** El sistema detecta y muestra todos los nombres que compartan la longitud máxima.
   - Ajuste gramatical automático (Singular/Plural) en el mensaje de respuesta.

## 🛠️ Tecnologías Utilizadas
- **Python 3.x**: Lógica de programación y estructuras de control.
- **Flask**: Framework para la gestión de rutas y renderizado de plantillas.
- **HTML5**: Estructuración semántica de formularios.
- **CSS3**: Diseño responsivo y centrado mediante Flexbox para una mejor experiencia de usuario.
- **Git/GitHub**: Control de versiones.

## 📁 Estructura del Proyecto
Siguiendo los lineamientos del material de estudio, el proyecto se organiza de la siguiente manera:
- `/Raíz`: Directorio principal del proyecto.
  - `main.py`: Archivo principal con las rutas y lógica de Python.
  - `/templates`: Carpeta que contiene las plantillas HTML (index, ejercicio1, ejercicio2).

## 💻 Instalación y Ejecución
1. Clonar el repositorio.
2. Crear un entorno virtual: `python -m venv venv`.
3. Instalar Flask: `pip install flask`.
4. Ejecutar la aplicación: `python main.py`.
5. Acceder a: `http://127.0.0.1:5000`.

---
**Desarrollado por:** Camila Zelada
**Institución:** IPLACEX
