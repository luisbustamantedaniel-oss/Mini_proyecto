import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.info_sistema import obtener_info_sistema, obtener_info_hardware
from modules.procesos import listar_procesos_activos, buscar_proceso, finalizar_proceso
from modules.organizador import organizar_carpeta
from modules.backup import realizar_respaldo
from modules.reporte import generar_reporte_txt
from modules.automatizacion import iniciar_tareas_programadas

def main():

    iniciar_tareas_programadas()
    
    while True:
        print("\n" + "="*45)
        print("    SYSADMIN ASSISTANT - MENÚ PRINCIPAL")
        print("="*45)
        print("1. Ver Información del Equipo y Hardware")
        print("2. Administrar Procesos Activos")
        print("3. Organizar una Carpeta Automáticamente")
        print("4. Crear Copia de Seguridad (Backup)")
        print("5. Generar Reporte General en TXT")
        print("6. Salir")
        print("="*45)
        
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            print("\n--- INFO SISTEMA ---")
            for k, v in obtener_info_sistema().items(): print(f"{k.upper()}: {v}")
            print("\n--- INFO HARDWARE ---")
            for k, v in obtener_info_hardware().items(): print(f"{k.upper()}: {v}")
            
        elif opcion == "2":
            print("\n1. Listar Procesos (Top 15)\n2. Buscar y finalizar un proceso")
            sub_opc = input("Opción: ")
            if sub_opc == "1":
                for p in listar_procesos_activos():
                    print(f"PID: {p['pid']} | Nombre: {p['nombre']} | CPU: {p['uso_cpu']}% | RAM: {p['uso_memoria']}%")
            elif sub_opc == "2":
                nombre = input("Nombre del proceso a buscar: ")
                encontrados = buscar_proceso(nombre)
                for proc in encontrados:
                    print(f"-> PID: {proc['pid']} | Nombre: {proc['name']}")
                if encontrados:
                    pid = int(input("Ingrese el PID del proceso que desea cerrar: "))
                    exito, msg = finalizar_proceso(pid)
                    print(msg)
                else:
                    print("No se encontraron procesos.")
                    
        elif opcion == "3":
            ruta = input("Ingrese la ruta de la carpeta a organizar: ")
            exito, msg = organizar_carpeta(ruta)
            print(msg)
            
        elif opcion == "4":
            orig = input("Ruta de la carpeta ORIGEN: ")
            dest = input("Ruta de la carpeta DESTINO: ")
            exito, resultado = realizar_respaldo(orig, dest)
            if exito:
                print(f"¡Respaldo Exitoso! Guardado en: {resultado['destino']}")
            else:
                print(f"Error: {resultado}")
                
        elif opcion == "5":
            exito, msg = generar_reporte_txt()
            print(msg)
            
        elif opcion == "6":
            print("Saliendo de la aplicación. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()