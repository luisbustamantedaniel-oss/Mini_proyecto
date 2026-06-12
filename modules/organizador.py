from pathlib import Path
import shutil

MAPEO_CATEGORIAS = {
    "Documentos": [".pdf", ".docx", ".xlsx", ".txt", ".pptx"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mkv"]
}

def organizar_carpeta(ruta_objetivo):
    ruta = Path(ruta_objetivo)
    if not ruta.exists() or not ruta.is_dir():
        return False, "La ruta especificada no es válida."

    conteo = 0
    for elemento in ruta.iterdir():
        if elemento.is_file():
            extension = elemento.suffix.lower()
            categoria_destino = "Otros"
            
            for categoria, extensiones in MAPEO_CATEGORIAS.items():
                if extension in extensiones:
                    categoria_destino = categoria
                    break
            
            carpeta_destino = ruta / categoria_destino
            carpeta_destino.mkdir(exist_ok=True)
            
            try:
                shutil.move(str(elemento), str(carpeta_destino / elemento.name))
                conteo += 1
            except Exception:
                continue
                
    return True, f"Organización completada. Se movieron {conteo} archivos."