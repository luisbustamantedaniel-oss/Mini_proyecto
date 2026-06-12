from pathlib import Path
import shutil
from datetime import datetime

def realizar_respaldo(ruta_origen, ruta_destino):
    origen = Path(ruta_origen)
    destino = Path(ruta_destino)
    
    if not origen.exists():
        return False, 
    
    try:
        marca_tiempo = datetime.now().strftime("%Y%m%d_%H%M%S")
        carpeta_final_respaldo = destino / f"Backup_{origen.name}_{marca_tiempo}"
        
        shutil.copytree(origen, carpeta_final_respaldo)
        num_archivos = sum(1 for p in carpeta_final_respaldo.rglob('*') if p.is_file())
        
        log_registro = {
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "hora": datetime.now().strftime("%H:%M:%S"),
            "archivos_copiados": num_archivos,
            "destino": str(carpeta_final_respaldo)
        }
        return True, log_registro
    except Exception as e:
        return False, str(e)