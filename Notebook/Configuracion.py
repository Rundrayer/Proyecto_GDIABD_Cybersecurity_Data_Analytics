#CONFIGURACION DE RUTAS DE PROYECTO

#
from pathlib import Path
import os


#MODIFICAR RUTAS CON LOS ARCHIVOS winutils.exe y hadoop.dll -------------------------------------------------------------------MODIFICAR
RUTA_HADOOP = Path(r"C:\Users\galle\Desktop\IA Datos\Jupyter\Proyecto_GDIABD_Cybersecurity_Data_Analytics\Recursos\hadoop")

#--

# Asignación automática de variables de entorno para PySpark/Hadoop
if RUTA_HADOOP.exists():
  os.environ["HADOOP_HOME"] = str(RUTA_HADOOP.resolve())
  os.environ["PATH"] = (
      os.environ["HADOOP_HOME"] + r"\bin;" + os.environ.get("PATH", "")
  )
else:
  print(
      f"ADVERTENCIA: La ruta de Hadoop '{RUTA_HADOOP}' no existe. Revisa Configuracion.py"
  )


#APUNTA A LA CARPETA "Datos" UBICADA JUNTO CON ESTE PROYECTO
DIRECTORIO_BASE = Path("../Datos") 

#APUNTA A LA CARPETA "Recursos" UBICADA JUNTO CON ESTE PROYECTO
RECURSOS = Path("../Recursos")

#DECLARACION DE RUTAS DE CARPETAS
CARGADOS = DIRECTORIO_BASE / "Cargados"
PROCESADOS = DIRECTORIO_BASE / "Procesados"
CSV_GENERADOS = DIRECTORIO_BASE / "CSV_Generados"
IMPLEMENTACION_GOBERNANZA = DIRECTORIO_BASE / "Implementacion_Gobernanza"
ANALITICOS_PARQUET = DIRECTORIO_BASE / "Analiticos" / "Parquet"
ANALITICOS_RESULTADOS = DIRECTORIO_BASE / "Analiticos" / "Resultados"

#LISTA DE RUTAS PARA CREAR CARPETAS SEGEMENTADAS
modelo_carpetas = [
    CARGADOS, PROCESADOS, CSV_GENERADOS,
    IMPLEMENTACION_GOBERNANZA, ANALITICOS_PARQUET, ANALITICOS_RESULTADOS
]

#CREACION DE CARPETAS
for modelo_carpeta in modelo_carpetas:
    modelo_carpeta.mkdir(parents=True, exist_ok=True)