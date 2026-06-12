import os
import platform
import socket
import psutil

def obtener_info_sistema():
    try:
        return {
            "nombre_equipo": socket.gethostname(),
            "usuario_actual": os.getlogin(),
            "sistema_operativo": platform.system(),
            "version_so": platform.version(),
            "arquitectura": platform.machine(),
            "direccion_ip": socket.gethostbyname(socket.gethostname())
        }
    except Exception as e:
        return {"error": f"No se pudo obtener la info del sistema: {e}"}

def obtener_info_hardware():
    try:
        ram = psutil.virtual_memory()
        disco = psutil.disk_usage('/')
        
        return {
            "ram_total_gb": round(ram.total / (1024**3), 2),
            "ram_utilizada_gb": round(ram.used / (1024**3), 2),
            "ram_libre_gb": round(ram.available / (1024**3), 2),
            "uso_cpu_porcentaje": psutil.cpu_percent(interval=0.5),
            "disco_total_gb": round(disco.total / (1024**3), 2),
            "disco_utilizado_gb": round(disco.used / (1024**3), 2),
            "disco_libre_gb": round(disco.free / (1024**3), 2)
        }
    except Exception as e:
        return {"error": f"No se pudo obtener la info del hardware: {e}"}