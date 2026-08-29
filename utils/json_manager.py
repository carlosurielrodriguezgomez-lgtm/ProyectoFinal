import json
from datetime import datetime
import os

RUTA_JSON = "data/auditoria.json"

def auditar_operacion(accion: str, detalle: str):
    registro = {
        "fecha": datetime.now().isoformat(),
        "accion": accion,
        "detalle": detalle
    }
    
    datos = []
    if os.path.exists(RUTA_JSON):
        with open(RUTA_JSON, 'r', encoding='utf-8') as file:
            try:
                datos = json.load(file)
            except json.JSONDecodeError:
                pass
                
    datos.append(registro)
    
    with open(RUTA_JSON, 'w', encoding='utf-8') as file:
        json.dump(datos, file, indent=4)