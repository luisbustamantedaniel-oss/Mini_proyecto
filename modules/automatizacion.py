import schedule
import time
import threading
from modules.reporte import generar_reporte_txt

def bucle_ejecucion():
    while True:
        schedule.run_pending()
        time.sleep(1)

def iniciar_tareas_programadas():
    schedule.every(1).minutes.do(generar_reporte_txt)
    
    hilo = threading.Thread(target=bucle_ejecucion, daemon=True)
    hilo.start()