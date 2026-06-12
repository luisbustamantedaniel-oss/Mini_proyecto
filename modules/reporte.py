from datetime import datetime
from modules.info_sistema import obtener_info_sistema, obtener_info_hardware

def generar_reporte_txt(ruta_salida="reporte_sistema.txt"):
    info_so = obtener_info_sistema()
    info_hw = obtener_info_hardware()
    
    try:
        with open(ruta_salida, "w", encoding="utf-8") as archivo:
            archivo.write("=========================================\n")
            archivo.write("       SYSADMIN ASSISTANT - REPORT       \n")
            archivo.write("=========================================\n")
            archivo.write(f"Generado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            archivo.write("--- INFORMACIÓN DEL SISTEMA ---\n")
            for k, v in info_so.items():
                archivo.write(f"{k.upper()}: {v}\n")
                
            archivo.write("\n--- RECURSOS DE HARDWARE ---\n")
            for k, v in info_hw.items():
                archivo.write(f"{k.upper()}: {v}\n")
        return True, f"Reporte guardado con éxito en: {ruta_salida}"
    except Exception as e:
        return False, str(e)