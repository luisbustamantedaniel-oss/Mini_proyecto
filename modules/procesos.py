import psutil

def listar_procesos_activos():
    procesos = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info
            procesos.append({
                "pid": info['pid'],
                "nombre": info['name'],
                "uso_cpu": info['cpu_percent'],
                "uso_memoria": round(info['memory_percent'] or 0, 2)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return procesos[:15]

def buscar_proceso(nombre_proceso):
    encontrados = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if nombre_proceso.lower() in proc.info['name'].lower():
                encontrados.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return encontrados

def finalizar_proceso(pid):
    procesos_criticos = ["system", "svchost.exe", "init", "explorer.exe"]
    try:
        p = psutil.Process(pid)
        if p.name().lower() in procesos_criticos:
            return False, 
        p.terminate()
        return True, f"Proceso {pid} finalizado correctamente."
    except psutil.NoSuchProcess:
        return False, 
    except psutil.AccessDenied:
        return False, 