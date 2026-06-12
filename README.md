# SYSADMIN ASSISTANT 
### Sistema Inteligente de Automatización y Monitoreo del Sistema Operativo con Python

Este proyecto es una herramienta modular desarrollada en Python diseñada para simplificar y automatizar tareas esenciales de administración y supervisión en sistemas operativos. Su enfoque principal es simular una aplicación real que sirva de apoyo técnico a usuarios avanzados o administradores de sistemas en pequeñas organizaciones.

---

## Tecnologías Obligatorias Utilizadas
El sistema fue construido utilizando las siguientes tecnologías y librerías:
* **Python 3.12+**
* **psutil:** Monitoreo y control de procesos activos y recursos de hardware.
* **shutil / os / pathlib:** Gestión avanzada de archivos, directorios y copias de seguridad.
* **schedule:** Planificación y automatización de tareas en segundo plano.
* **threading:** Manejo de hilos independientes para evitar el bloqueo de la interfaz.
* **datetime / socket / platform:** Captura de métricas de red, sistema operativo y marcas de tiempo.

---

## Estructura del Proyecto
El software sigue una arquitectura completamente modular para garantizar las buenas prácticas de programación:

```text
Proyecto_S_Operativos/
│
├── main.py                 # Punto de entrada principal e interfaz de consola.
├── README.md               # Documentación general del repositorio.
└── modules/                # Paquete contenedor de la lógica del negocio.
    ├── __init__.py         # Archivo de inicialización de paquete (vacío).
    ├── info_sistema.py     # Módulo 1: Captura de datos del SO y Hardware.
    ├── monitor_procesos.py # Módulo 2: Monitoreo, búsqueda y cierre de procesos.
    ├── organizador.py      # Módulo 3: Clasificación automática de directorios.
    ├── backup.py           # Módulo 4: Sistema de respaldos con logs.
    ├── reportes.py         # Módulo 5: Generación de registros analíticos en .txt.
    └── automatizacion.py   # Módulo 6: Planificador de hilos en segundo plano.
